# Integração Banco Inter (mTLS)

Este backend expõe um proxy seguro (mTLS) para a API do Banco Inter com exemplos de PIX, Boletos, Webhook e Extrato.

## Como configurar

1) Coloque o certificado:
- Recomendado: `.pfx` em `./secrets/` (não é commitado)

2) Variáveis de ambiente (`.env`):

```
INTER_API_BASE=https://cdpj.partners.bancointer.com.br
# Opção PFX
INTER_API_PFX=./secrets/avila-certificado.pfx
INTER_API_PFX_PASSWORD=senha-do-pfx

# Opção PEM
#INTER_API_CERT_PEM=./secrets/avila-cert.crt
#INTER_API_KEY_PEM=./secrets/avila-key.key

# OAuth2 (se o produto/rota exigir)
#INTER_API_TOKEN_URL=https://cdpj.partners.bancointer.com.br/oauth/token
#INTER_API_CLIENT_ID=...
#INTER_API_CLIENT_SECRET=...
#INTER_API_SCOPE=...
```

3) Instale dependências:

```powershell
python -m pip install -r requirements.txt
```

4) Rode o servidor:

```powershell
python -m uvicorn backend.server:app --host 127.0.0.1 --port 8000 --reload
```

## Endpoints

- GET /health
- GET /inter/extrato?data_inicio=YYYY-MM-DD&data_fim=YYYY-MM-DD
- GET /inter/get?path=/banking/v2/extrato&data_inicio=...&data_fim=...
- POST /inter/post?path=/pix/v2/cob {...}
- PUT /inter/put?path=/pix/v2/webhook/{chave} {...}
- DELETE /inter/delete?path=/pix/v2/webhook/{chave}

PIX
- POST /pix/cobrancas { json da cobrança }
- GET /pix/cobrancas/{txid}
- POST /pix/qrcode { json }
- GET /pix?inicio=...&fim=...&cpf_cnpj=opcional
- PUT /pix/devolucao/{e2eid}/{devolucao_id} { json }
- PUT /pix/webhook/{chave}?url=https://seuservidor/webhook
- GET /pix/webhook/{chave}
- DELETE /pix/webhook/{chave}

Boletos
- POST /boletos { json do boleto }
- GET /boletos/{nosso_numero}
- GET /boletos/{nosso_numero}/pdf
- POST /boletos/{nosso_numero}/baixa { json }

Observações
- Os paths podem variar conforme a versão do produto. Ajuste conforme o documento do Inter que você anexou.
- Em rotas que exigem OAuth2, preencha INTER_API_TOKEN_URL, CLIENT_ID, CLIENT_SECRET e SCOPE.
- O PDF está retornado como texto (latin1) para simplificar. Posso retornar base64 binário ou content-type application/pdf, como preferir.
