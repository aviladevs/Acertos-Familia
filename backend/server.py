from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from .db import Database, DBConfig
from typing import Optional, Dict, Any
import os

load_dotenv()
app = FastAPI(title="Avila DevOps API", version="0.1.0")

# Configurar CORS com domínios específicos
cors_origins = os.getenv("CORS_ORIGINS", "https://aviladevs.github.io,http://127.0.0.1:5500").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Montar arquivos estáticos (frontend)
app.mount("/", StaticFiles(directory="../", html=True), name="static")

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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
