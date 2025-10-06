#!/bin/bash
# Script de deploy para avilatransportes.com.br

echo "🚀 DEPLOY PARA AVILATRANSPORTES.COM.BR"
echo "======================================"

echo "✅ Verificando arquivos..."
FILES=(
    "index.html"
    "login.html" 
    "acertos.html"
    "analise.html"
    "extratos.js"
    "dados-exemplo.js"
    ".htaccess"
    "package.json"
)

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file - OK"
    else
        echo "❌ $file - FALTANDO"
    fi
done

echo ""
echo "🔒 ATENÇÃO: ALTERAR SENHAS ANTES DO DEPLOY!"
echo "Editar login.html linhas 142-157"
echo ""
echo "📤 UPLOAD VIA FTP/CPANEL:"
echo "Destino: /public_html/acertos/"
echo ""
echo "🌐 URL FINAL:"
echo "https://avilatransportes.com.br/acertos/"