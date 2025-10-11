#!/usr/bin/env bash
set -euo pipefail

#!/bin/bash
set -e

echo "🚀 Iniciando Avila Transportes API..."

# Criar diretório de dados se não existir
mkdir -p /data

# Default DB path (Railway volume-friendly)
export DB_PATH="${DB_PATH:-/data/clientes.db}"

# Start server on Railway-provided PORT
export PORT=${PORT:-8000}
exec uvicorn backend.server:app --host 0.0.0.0 --port "$PORT"
