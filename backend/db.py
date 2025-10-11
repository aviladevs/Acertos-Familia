import os
import sqlite3
from dataclasses import dataclass
from typing import Iterable, List, Dict, Any, Optional


@dataclass
class DBConfig:
    path: str

    @staticmethod
    def from_env() -> "DBConfig":
        path = os.getenv("DB_PATH", os.path.join(os.getcwd(), "data", "clientes.db"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        return DBConfig(path)


class Database:
    def __init__(self, cfg: DBConfig | None = None) -> None:
        self.cfg = cfg or DBConfig.from_env()
        self._ensure()

    def _connect(self):
        return sqlite3.connect(self.cfg.path)

    def _ensure(self) -> None:
        with self._connect() as conn:
            # Tabela de usuários
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    role TEXT NOT NULL DEFAULT 'user',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            # Tabela de transações (existente)
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS transacoes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT NOT NULL,
                    cnpj_cpf TEXT,
                    cliente TEXT,
                    valor REAL NOT NULL,
                    descricao TEXT,
                    origem TEXT,
                    UNIQUE(data, valor, descricao, origem) ON CONFLICT IGNORE
                )
                """
            )

    # ==================
    # Gestão de Usuários
    # ==================
    def reset_usuarios(self) -> None:
        """Remove todos os usuários e cria um administrador padrão."""
        with self._connect() as conn:
            # Remove todos os usuários
            conn.execute("DELETE FROM usuarios")
            # Cria usuário administrador (senha: 'admin123' - mude em produção!)
            conn.execute(
                "INSERT INTO usuarios (username, password_hash, role) VALUES (?, ?, ?)",
                ("nicolasrosaab", "pbkdf2:sha256:260000$example$saltedhash", "admin")
            )
            conn.commit()

    def autenticar_usuario(self, username: str, password: str) -> Optional[Dict[str, Any]]:
        """Autentica um usuário. Retorna dados do usuário se válido."""
        # Nota: Em produção, use hashing seguro como bcrypt
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT id, username, role FROM usuarios WHERE username = ? AND password_hash = ?",
                (username, password)  # Simplificado; use hash real
            )
            row = cur.fetchone()
            if row:
                return {"id": row[0], "username": row[1], "role": row[2]}
            return None

    def listar_usuarios(self) -> List[Dict[str, Any]]:
        """Lista todos os usuários (apenas para admin)."""
        with self._connect() as conn:
            cur = conn.execute("SELECT id, username, role, created_at FROM usuarios")
            cols = [c[0] for c in cur.description]
            return [dict(zip(cols, row)) for row in cur.fetchall()]

    # ==================
    # Transações (existente)
    # ==================
    def inserir_transacoes(self, itens: Iterable[Dict[str, Any]]) -> int:
        rows = [
            (
                x.get("data"),
                x.get("cnpj_cpf"),
                x.get("cliente"),
                float(x.get("valor", 0) or 0),
                x.get("descricao"),
                x.get("origem", "admin"),
            )
            for x in itens
        ]
        with self._connect() as conn:
            cur = conn.executemany(
                "INSERT OR IGNORE INTO transacoes (data, cnpj_cpf, cliente, valor, descricao, origem) VALUES (?, ?, ?, ?, ?, ?)",
                rows,
            )
            return cur.rowcount or 0

    def listar_transacoes(self, limit: int = 1000) -> List[Dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT data, cnpj_cpf, cliente, valor, descricao, origem FROM transacoes ORDER BY data DESC, rowid DESC LIMIT ?",
                (limit,),
            )
            cols = [c[0] for c in cur.description]
            return [dict(zip(cols, row)) for row in cur.fetchall()]
