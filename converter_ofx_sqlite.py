#!/usr/bin/env python3
"""
Conversão de extratos bancários (CSV/OFX) para SQLite.

Recursos:
- Lê múltiplos arquivos .csv e .ofx
- Normaliza datas e valores
- Extrai CPF/CNPJ e nome/razão social da descrição
- Remove duplicidades por (data, cnpj_cpf, valor)
- Grava em clientes.db na tabela transacoes e uma tabela por cliente (cliente_<cnpj_cpf>)

Uso rápido (no Windows PowerShell):
  python converter_ofx_sqlite.py --input .
  python converter_ofx_sqlite.py --input NU_*.ofx Extrato*.ofx *.csv

Dependências: pandas, ofxparse
"""
from __future__ import annotations

import argparse
import os
import re
import sqlite3
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple

import pandas as pd

try:
    from ofxparse import OfxParser  # type: ignore
except Exception:  # pragma: no cover - fallback opcional
    OfxParser = None  # type: ignore


# =====================
# Utilidades de parsing
# =====================

RE_ONLY_DIGITS = re.compile(r"\D+")
RE_CPF = re.compile(r"\b(\d{3}\.?\d{3}\.?\d{3}-?\d{2}|\d{11})\b")
RE_CNPJ = re.compile(r"\b(\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}|\d{14})\b")


def norm_digits(text: str) -> str:
    return RE_ONLY_DIGITS.sub("", text or "")


def is_cpf(value: str) -> bool:
    digits = norm_digits(value)
    return len(digits) == 11


def is_cnpj(value: str) -> bool:
    digits = norm_digits(value)
    return len(digits) == 14


def extrair_cnpj_cpf(texto: str) -> Optional[str]:
    if not texto:
        return None
    for rx in (RE_CNPJ, RE_CPF):
        m = rx.search(texto)
        if m:
            return norm_digits(m.group(1))
    return None


def extrair_nome(texto: str, documento: Optional[str] = None) -> Optional[str]:
    if not texto:
        return None
    nome = texto
    # Remove documento (formatado ou só dígitos)
    if documento:
        dnum = norm_digits(documento)
        if is_cpf(dnum):
            nome = re.sub(rf"{dnum[:3]}\.?{dnum[3:6]}\.?{dnum[6:9]}-?{dnum[9:]}|{dnum}", "", nome)
        elif is_cnpj(dnum):
            nome = re.sub(rf"{dnum[:2]}\.?{dnum[2:5]}\.?{dnum[5:8]}/?{dnum[8:12]}-?{dnum[12:]}|{dnum}", "", nome)

    # Remove datas dd/mm/yyyy
    nome = re.sub(r"\b\d{2}/\d{2}/\d{4}\b", "", nome)
    # Mantém apenas letras/espacos
    nome = re.sub(r"[^A-Za-zÀ-ÖØ-öø-ÿ\s]", " ", nome)
    nome = re.sub(r"\s+", " ", nome).strip()
    if not nome:
        return None
    # Limita tamanho e capitaliza básico
    partes = nome.split()
    nome = " ".join(partes[:6])
    return nome.title()


def parse_valor(texto: str) -> Optional[float]:
    if texto is None:
        return None
    s = str(texto).strip()
    if not s:
        return None
    # Normaliza formatos BR/US
    s = s.replace("R$", "").replace(" ", "")
    # Se tiver vírgula e ponto, assume BR
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s and "." not in s:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def parse_data(texto: str) -> Optional[str]:
    if not texto:
        return None
    s = str(texto).strip()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%Y%m%d", "%d-%m-%Y", "%d.%m.%Y"):
        try:
            return datetime.strptime(s[:10], fmt).strftime("%Y-%m-%d")
        except Exception:
            pass
    # Caso OFX: 20250105XXXX
    m = re.match(r"(\d{4})(\d{2})(\d{2})", s)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    return None


# =====================
# Leitura de arquivos
# =====================


def carregar_csv(path: Path) -> pd.DataFrame:
    last_err: Optional[Exception] = None
    for enc in ("utf-8", "latin-1"):
        try:
            df = pd.read_csv(path, sep=None, engine="python", encoding=enc)
            break
        except Exception as e:  # tenta proximo encoding
            last_err = e
            continue
    else:
        raise last_err or RuntimeError(f"Falha ao ler CSV: {path}")

    # Mapeia colunas prováveis
    cols = {c.lower().strip(): c for c in df.columns}
    def find(*keys: str) -> Optional[str]:
        for k in keys:
            if k in cols:
                return cols[k]
        return None

    c_data = find("data", "data lancamento", "date")
    c_desc = find("descricao", "descrição", "history", "memo", "nome", "identificacao")
    c_val = find("valor", "amount", "valor r$", "value")

    if not (c_data and c_desc and c_val):
        # tenta heurística Inter comum: Data Lancamento;Descricao;Valor;Saldo
        if len(df.columns) >= 3:
            c_data, c_desc, c_val = df.columns[:3]
        else:
            raise RuntimeError(f"CSV sem colunas reconhecíveis: {path}")

    out = pd.DataFrame({
        "data": df[c_data].apply(parse_data),
        "valor": df[c_val].apply(parse_valor),
        "descricao": df[c_desc].fillna("").astype(str),
    })
    out.dropna(subset=["data", "valor"], inplace=True)
    return out


def carregar_ofx(path: Path) -> pd.DataFrame:
    if OfxParser is not None:
        try:
            with open(path, "r", encoding="utf-8") as f:
                ofx = OfxParser.parse(f)
            registros = []
            for t in ofx.account.statement.transactions:
                registros.append({
                    "data": t.date.strftime("%Y-%m-%d"),
                    "valor": float(t.amount),
                    "descricao": (t.memo or t.payee or "").strip(),
                })
            return pd.DataFrame(registros)
        except Exception:
            pass  # tenta fallback simples

    # Fallback por regex simples de tags
    text = Path(path).read_text(encoding="utf-8", errors="ignore")
    itens = re.findall(r"<STMTTRN>([\s\S]*?)</STMTTRN>", text, flags=re.IGNORECASE)
    registros = []
    for bloco in itens:
        d = re.search(r"<DTPOSTED>([^<]+)", bloco, flags=re.IGNORECASE)
        v = re.search(r"<TRNAMT>([^<]+)", bloco, flags=re.IGNORECASE)
        m = re.search(r"<(MEMO|NAME)>([^<]+)", bloco, flags=re.IGNORECASE)
        data = parse_data(d.group(1)) if d else None
        valor = parse_valor(v.group(1)) if v else None
        desc = m.group(2).strip() if m else ""
        if data is not None and valor is not None:
            registros.append({"data": data, "valor": valor, "descricao": desc})
    return pd.DataFrame(registros)


# =====================
# Pipeline principal
# =====================


def processar_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["cnpj_cpf"] = df["descricao"].apply(extrair_cnpj_cpf)
    df["cliente"] = [
        extrair_nome(desc, doc) if (doc := extrair_cnpj_cpf(desc)) else extrair_nome(desc)
        for desc in df["descricao"].astype(str)
    ]
    # Deduplicação básica
    df.drop_duplicates(subset=["data", "valor", "descricao"], inplace=True)
    return df[["data", "cnpj_cpf", "cliente", "valor", "descricao"]]


def salvar_sqlite(df: pd.DataFrame, db_path: Path) -> None:
    db_path = Path(db_path)
    conn = sqlite3.connect(str(db_path))
    try:
        # Cria tabela principal com tipos e índice
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS transacoes (
                data TEXT NOT NULL,
                cnpj_cpf TEXT,
                cliente TEXT,
                valor REAL NOT NULL,
                descricao TEXT,
                UNIQUE(data, valor, descricao) ON CONFLICT IGNORE
            )
            """
        )
        df.to_sql("transacoes", conn, if_exists="append", index=False)

        # Uma tabela por cliente
        for cnpj_cpf, grupo in df.groupby("cnpj_cpf"):
            if not cnpj_cpf:
                continue
            tbl = f"cliente_{cnpj_cpf}"
            grupo.to_sql(tbl, conn, if_exists="replace", index=False)
    finally:
        conn.close()


def discover_files(patterns: Sequence[str]) -> List[Path]:
    files: List[Path] = []
    for p in patterns:
        # Expande diretórios em glob padrão
        if os.path.isdir(p):
            root = Path(p)
            files.extend(sorted(root.glob("**/*.csv")))
            files.extend(sorted(root.glob("**/*.ofx")))
        else:
            files.extend([Path(x) for x in Path().glob(p)])
    # Remove duplicados preservando ordem
    seen = set()
    uniq: List[Path] = []
    for f in files:
        if f not in seen and f.exists():
            uniq.append(f)
            seen.add(f)
    return uniq


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Converter CSV/OFX para SQLite")
    ap.add_argument("--input", "-i", nargs="+", default=["."], help="Arquivos ou pastas (glob)")
    ap.add_argument("--db", default="clientes.db", help="Caminho do SQLite de saída")
    args = ap.parse_args(argv)

    paths = discover_files(args.input)
    if not paths:
        print("Nenhum arquivo .csv/.ofx encontrado.")
        return 1

    frames: List[pd.DataFrame] = []
    for p in paths:
        try:
            if p.suffix.lower() == ".csv":
                df = carregar_csv(p)
            elif p.suffix.lower() == ".ofx":
                df = carregar_ofx(p)
            else:
                continue
            if not df.empty:
                frames.append(df)
                print(f"OK: {p} -> {len(df)} registros")
        except Exception as e:
            print(f"ERRO: {p}: {e}")

    if not frames:
        print("Nada para salvar.")
        return 2

    df_all = pd.concat(frames, ignore_index=True)
    df_all = processar_df(df_all)
    salvar_sqlite(df_all, Path(args.db))
    print(f"SQLite salvo em: {args.db} / Linhas: {len(df_all)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
