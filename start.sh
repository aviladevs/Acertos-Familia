#!/usr/bin/env bash
set -euo pipefail

#!/bin/bash
set -e

echo "🚀 Iniciando Avila Transportes API..."

# Criar diretório de dados se não existir
mkdir -p /data

# Decodificar certificados do Base64
if [ -n "$INTER_API_CERT_BASE64" ] && [ -n "$INTER_API_KEY_BASE64" ]; then
    echo "📜 Decodificando certificados CRT/KEY..."
    echo "$INTER_API_CERT_BASE64" | base64 -d > /tmp/certificado.crt
    echo "$INTER_API_KEY_BASE64" | base64 -d > /tmp/chave.key
    export INTER_API_CERT_PEM="/tmp/certificado.crt"
    export INTER_API_KEY_PEM="/tmp/chave.key"
    echo "✅ Certificados CRT/KEY configurados"
else
    echo "⚠️  Certificados Base64 não encontrados - usando certificados locais"
fi

# Decode PEM cert/key if provided as BASE64
if [ -n "${INTER_API_CERT_PEM_BASE64:-}" ]; then
  echo "$INTER_API_CERT_PEM_BASE64" | base64 -d > /tmp/inter_cert.pem
  export INTER_API_CERT_PEM=/tmp/inter_cert.pem
fi
if [ -n "${INTER_API_KEY_PEM_BASE64:-}" ]; then
  echo "$INTER_API_KEY_PEM_BASE64" | base64 -d > /tmp/inter_key.pem
  export INTER_API_KEY_PEM=/tmp/inter_key.pem
fi

# Default DB path (Railway volume-friendly)
export DB_PATH="${DB_PATH:-/data/clientes.db}"

# Start server on Railway-provided PORT
export PORT=${PORT:-8000}
exec uvicorn backend.server:app --host 0.0.0.0 --port "$PORT"
