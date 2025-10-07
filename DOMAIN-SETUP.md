# Configuração de Domínio - avilatransportes.com.br

## 📋 Resumo
Esta documentação explica como configurar o domínio `avilatransportes.com.br` para o sistema completo.

## 🌐 Estrutura de Domínios

### Frontend (GitHub Pages)
- **Domínio**: `avilatransportes.com.br`
- **CNAME**: Já configurado para GitHub Pages
- **Funcionalidade**: Interface web, formulários, visualizações

### Backend (Railway)  
- **Domínio**: `api.avilatransportes.com.br`
- **Destino**: Projeto Railway
- **Funcionalidade**: API FastAPI, integração Inter, banco de dados

## ⚙️ Configuração DNS

### 1. Configurar CNAME para API
```
CNAME api.avilatransportes.com.br → seu-projeto.up.railway.app
```

### 2. Verificar configuração atual
```
CNAME avilatransportes.com.br → aviladevs.github.io (já configurado)
```

## 🚀 Configuração Railway

### 1. Domínio Customizado
1. Acesse Railway Dashboard
2. Vá para Settings > Environment 
3. Configure Custom Domain: `api.avilatransportes.com.br`

### 2. Variáveis de Ambiente
Copie do arquivo `RAILWAY-VARS.txt`:
```bash
PRODUCTION_DOMAIN=https://api.avilatransportes.com.br
FRONTEND_DOMAIN=https://avilatransportes.com.br
CORS_ORIGINS=https://avilatransportes.com.br,http://127.0.0.1:5500
PORT=8000
```

## 🔧 Configuração Frontend

### Admin Interface
O admin já está configurado para usar:
- **Produção**: `https://api.avilatransportes.com.br`
- **Local**: `http://127.0.0.1:8000`

### Autocomplete
✅ Implementado com busca em cadastros com flag "conta corrente"
- Campos De/Para agora mostram sugestões
- Filtra apenas cadastros com conta corrente ativa
- Busca por nome e documento

## 📱 Funcionalidades Implementadas

### 1. Sistema de Cadastro
- ✅ Campo "Conta Corrente" adicionado
- ✅ Filtragem por conta corrente
- ✅ Visualização de status na tabela

### 2. Autocomplete
- ✅ Campos De/Para com sugestões
- ✅ Busca em tempo real
- ✅ Seleção por clique
- ✅ Interface responsiva

### 3. Configuração de Domínio
- ✅ Backend configurado para api.avilatransportes.com.br
- ✅ CORS configurado para domínio específico
- ✅ Variáveis de ambiente preparadas

## 🔍 Teste de Configuração

### 1. Verificar DNS
```bash
nslookup api.avilatransportes.com.br
```

### 2. Testar API
```bash
curl https://api.avilatransportes.com.br/health
```

### 3. Verificar Frontend
- Acesse: https://avilatransportes.com.br
- Clique em "Admin"
- Verifique se a URL do backend está configurada

## 🚨 Próximos Passos

1. **Configurar DNS**: Adicionar CNAME para `api.avilatransportes.com.br`
2. **Railway Setup**: Configurar domínio customizado no Railway
3. **Certificado**: Inserir senha real do certificado PFX nas variáveis
4. **Teste**: Verificar funcionamento completo

## 💡 Dicas

- Use o admin interface para alternar entre local e produção
- O autocomplete só funciona com cadastros que têm "conta corrente" ativa
- Todas as configurações são salvas no localStorage do navegador