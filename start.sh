#!/usr/bin/env bash
set -euo pipefail

# Decode PFX cert if provided as BASE64
if [ -n "${INTER_API_PFX_BASE64:-}" ]; then
  echo "$INTER_API_PFX_BASE64" | base64 -d > /tmp/inter.pfx
  export INTER_API_PFX=/tmp/inter.pfx
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
