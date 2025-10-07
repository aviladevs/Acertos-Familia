from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from .inter_api_client import InterAPIClient, InterAPIConfig
from dotenv import load_dotenv
from .db import Database, DBConfig
from typing import Optional, Dict, Any

load_dotenv()
app = FastAPI(title="Avila Inter API Proxy", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = Database(DBConfig.from_env())


@app.get("/health")
def health():
    return {"status": "ok"}


# =========================
# Sincronização de transações
# =========================
@app.get("/sync/transacoes")
def sync_listar(limit: int = 1000):
    try:
        return {"items": db.listar_transacoes(limit=limit)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/sync/transacoes")
def sync_inserir(payload: Dict[str, Any]):
    try:
        itens = payload.get("items", [])
        inseridos = db.inserir_transacoes(itens)
        return {"inseridos": inseridos}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/inter/saldo")
def inter_saldo():
    try:
        client = InterAPIClient(InterAPIConfig.from_env())
        return client.obter_saldo()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/inter/extrato")
def inter_extrato(
    data_inicio: str = Query(None),
    data_fim: str = Query(None),
    inicio: str = Query(None),
    fim: str = Query(None),
):
    try:
        # Suporta aliases de parâmetros
        data_inicio = data_inicio or inicio
        data_fim = data_fim or fim
        if not data_inicio or not data_fim:
            raise HTTPException(status_code=422, detail="Parâmetros obrigatórios: data_inicio/data_fim (ou inicio/fim)")
        client = InterAPIClient(InterAPIConfig.from_env())
        return client.obter_extrato(data_inicio, data_fim)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/inter/extrato_mock")
def inter_extrato_mock(inicio: str = Query(...), fim: str = Query(...)):
    # Mock simples para testes de ponta a ponta sem mTLS
    try:
        items = [
            {"data": "2025-09-01", "descricao": "Pix Recebido: ACME LTDA 12.345.678/0001-99", "valor": 1250.55, "tipo": "C"},
            {"data": "2025-09-02", "descricao": "Transferência Enviada: SUPERMERCADO XYZ 34.567.890/0001-12", "valor": 230.70, "tipo": "D"},
            {"data": "2025-09-03", "descricao": "Pix Recebido: JOSE DA SILVA 123.456.789-00", "valor": 320.00, "tipo": "C"},
            {"data": "2025-09-04", "descricao": "Pagamento Boleto: CONDOMINIO SOLAR 11.222.333/0001-44", "valor": 650.00, "tipo": "D"},
            {"data": "2025-09-05", "descricao": "Pix Recebido: BETA SERVICOS LTDA 98.765.432/0001-10", "valor": 2100.00, "tipo": "C"},
            {"data": "2025-09-06", "descricao": "Transferência Enviada: FARMACIA SAUDE 22.333.444/0001-55", "valor": 89.90, "tipo": "D"},
            {"data": "2025-09-07", "descricao": "Pix Recebido: NUBANK PAGAMENTOS S.A. 18.236.120/0001-58", "valor": 415.35, "tipo": "C"},
            {"data": "2025-09-08", "descricao": "TED Enviada: POSTO PETRO 44.555.666/0001-77", "valor": 150.00, "tipo": "D"},
        ]
        return {"items": items, "inicio": inicio, "fim": fim, "fonte": "mock"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/inter/get")
def inter_get(path: str = Query(...), data_inicio: Optional[str] = None, data_fim: Optional[str] = None):
    try:
        client = InterAPIClient(InterAPIConfig.from_env())
        params: Dict[str, Any] = {}
        if data_inicio:
            params["dataInicio"] = data_inicio
        if data_fim:
            params["dataFim"] = data_fim
        return client.get(path, params=params or None).json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/inter/post")
def inter_post(path: str = Query(...), body: Optional[Dict[str, Any]] = None):
    try:
        client = InterAPIClient(InterAPIConfig.from_env())
        return client.post(path, json=body or {}).json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/inter/put")
def inter_put(path: str = Query(...), body: Optional[Dict[str, Any]] = None):
    try:
        client = InterAPIClient(InterAPIConfig.from_env())
        return client.put(path, json=body or {}).json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/inter/delete")
def inter_delete(path: str = Query(...)):
    try:
        client = InterAPIClient(InterAPIConfig.from_env())
        client.delete(path)
        return {"ok": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ==================
# PIX endpoints demo
# ==================
@app.post("/pix/cobrancas")
def pix_criar_cobranca(body: Dict[str, Any]):
    try:
        client = InterAPIClient(InterAPIConfig.from_env())
        return client.pix_criar_cobranca(body)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/pix/cobrancas/{txid}")
def pix_consultar_cobranca(txid: str):
    try:
        client = InterAPIClient(InterAPIConfig.from_env())
        return client.pix_consultar_cobranca(txid)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/pix/qrcode")
def pix_qrcode(body: Dict[str, Any]):
    try:
        client = InterAPIClient(InterAPIConfig.from_env())
        return client.pix_criar_qrcode(body)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/pix")
def pix_listar(inicio: str = Query(...), fim: str = Query(...), cpf_cnpj: Optional[str] = None):
    try:
        client = InterAPIClient(InterAPIConfig.from_env())
        return client.pix_listar(inicio, fim, cpf_cnpj)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/pix/devolucao/{e2eid}/{devolucao_id}")
def pix_devolver(e2eid: str, devolucao_id: str, body: Dict[str, Any]):
    try:
        client = InterAPIClient(InterAPIConfig.from_env())
        return client.pix_devolver(e2eid, devolucao_id, body)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/pix/webhook/{chave}")
def pix_webhook_registrar(chave: str, url: str = Query(...)):
    try:
        client = InterAPIClient(InterAPIConfig.from_env())
        return client.pix_webhook_registrar(chave, url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/pix/webhook/{chave}")
def pix_webhook_consultar(chave: str):
    try:
        client = InterAPIClient(InterAPIConfig.from_env())
        return client.pix_webhook_consultar(chave)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/pix/webhook/{chave}")
def pix_webhook_remover(chave: str):
    try:
        client = InterAPIClient(InterAPIConfig.from_env())
        client.pix_webhook_remover(chave)
        return {"ok": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ==================
# Boletos endpoints
# ==================
@app.post("/boletos")
def boleto_emitir(body: Dict[str, Any]):
    try:
        client = InterAPIClient(InterAPIConfig.from_env())
        return client.boleto_emitir(body)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/boletos/{nosso_numero}")
def boleto_consultar(nosso_numero: str):
    try:
        client = InterAPIClient(InterAPIConfig.from_env())
        return client.boleto_consultar(nosso_numero)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/boletos/{nosso_numero}/pdf")
def boleto_pdf(nosso_numero: str):
    try:
        client = InterAPIClient(InterAPIConfig.from_env())
        pdf = client.boleto_pdf(nosso_numero)
        return {"content_base64": pdf.decode("latin1")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/boletos/{nosso_numero}/baixa")
def boleto_baixa(nosso_numero: str, body: Dict[str, Any]):
    try:
        client = InterAPIClient(InterAPIConfig.from_env())
        return client.boleto_baixa(nosso_numero, body)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
