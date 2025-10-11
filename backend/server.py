from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
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

# Chamar reset de usuários na inicialização (apenas para setup inicial)
db.reset_usuarios()

# Segurança básica
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    # Simples verificação; em produção, use JWT ou similar
    token = credentials.credentials
    if token == "admin-token":  # Token fixo para admin
        return {"username": "nicolasrosaab", "role": "admin"}
    raise HTTPException(status_code=401, detail="Token inválido")


@app.get("/health")
def health():
    return {"status": "ok"}


# ==================
# Autenticação
# ==================
@app.post("/login")
def login(credentials: Dict[str, str]):
    username = credentials.get("username")
    password = credentials.get("password")
    user = db.autenticar_usuario(username, password)
    if user:
        return {"token": "admin-token", "user": user}  # Token fixo para simplicidade
    raise HTTPException(status_code=401, detail="Credenciais inválidas")


@app.get("/usuarios")
def listar_usuarios(current_user: Dict = Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Acesso negado")
    return db.listar_usuarios()


# ==================
# Gestão de Usuários (apenas admin)
# ==================
@app.post("/usuarios/reset")
def reset_usuarios_endpoint(current_user: Dict = Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Acesso negado")
    db.reset_usuarios()
    return {"message": "Usuários resetados com sucesso"}


# ==================
# Sincronização de transações (protegido)
# ==================
@app.get("/sync/transacoes")
def sync_listar(limit: int = 1000, current_user: Dict = Depends(get_current_user)):
    if current_user["role"] not in ["admin", "user"]:
        raise HTTPException(status_code=403, detail="Acesso negado")
    try:
        return {"items": db.listar_transacoes(limit=limit)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/sync/transacoes")
def sync_inserir(payload: Dict[str, Any], current_user: Dict = Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Acesso negado")
    try:
        itens = payload.get("items", [])
        inseridos = db.inserir_transacoes(itens)
        return {"inseridos": inseridos}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
