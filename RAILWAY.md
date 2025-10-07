# Deploy do Backend (FastAPI) no Railway

Este projeto inclui um backend FastAPI exposto em `backend/server.py`. A seguir, como subir no Railway.

## Requisitos
- Repositório no GitHub (este)
- Railway conta e projeto

## Variáveis de Ambiente

Defina as variáveis no Railway (Service > Variables):

Obrigatórias (um dos métodos):
- Método PFX:
  - `INTER_API_PFX_BASE64`: conteúdo do .pfx em Base64 (sem quebras)
  - `INTER_API_PFX_PASSWORD`: senha do PFX
- Método PEM:
  - `INTER_API_CERT_PEM_BASE64`: conteúdo do cert PEM em Base64
  - `INTER_API_KEY_PEM_BASE64`: conteúdo do key PEM em Base64

Opcionais:
- `INTER_API_BASE`: base da API do Inter (default: https://api.bancointer.com.br)
- `INTER_API_TOKEN_URL`, `INTER_API_CLIENT_ID`, `INTER_API_CLIENT_SECRET`, `INTER_API_SCOPE`: OAuth2 se necessário
- `INTER_API_TIMEOUT`: timeout (s)
- `DB_PATH`: caminho do SQLite (default: /data/clientes.db)

Sistema:
- `PORT`: variável que o Railway injeta automaticamente

## Build & Start

O Railway detecta `requirements.txt` e instala as deps. O processo web usa o `Procfile`:

```
web: bash start.sh
```

O script `start.sh` decodifica certificados (se passados em Base64) e sobe o Uvicorn:

```
uvicorn backend.server:app --host 0.0.0.0 --port $PORT
```

## Testes rápidos
- Health: `GET /health`
- Extrato mock (sem mTLS): `GET /inter/extrato_mock?inicio=2025-09-01&fim=2025-09-30`
- Extrato real (mTLS): `GET /inter/extrato?data_inicio=2025-09-01&data_fim=2025-09-30`

## CORS
CORS está liberado para `*` (ajuste se necessário em produção).

## Logs e Debug
Use os logs do Railway (Deploys > Logs) para checar erros de mTLS, certificados e OAuth.
