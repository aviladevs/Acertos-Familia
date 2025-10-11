#!/bin/bash
# Script de deploy para Railway - aviladevops.com.br

echo "🚀 DEPLOY PARA AVILADEVOPS.COM.BR"
echo "======================================"

echo "✅ Verificando arquivos essenciais..."
FILES=(
    "index.html"
    "login.html" 
    "acertos.html"
    "analise.html"
    "extratos.js"
    "backend/server.py"
    "backend/db.py"
    "requirements.txt"
    "Procfile"
    "start.sh"
)

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file - OK"
    else
        echo "❌ $file - FALTANDO"
    fi
done

echo ""
echo "📤 DEPLOY VIA GIT PUSH:"
echo "  git push origin main"
echo ""
echo "🚂 Railway fará deploy automático"
echo ""
echo "🌐 URL FINAL:"
echo "https://aviladevops.com.br"