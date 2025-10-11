# Ávila DevOps - Sistema de Controle Financeiro

Sistema completo para controle de acertos financeiros da família, desenvolvido pela equipe Ávila DevOps. Gerencia transações, análises financeiras e processa extratos bancários com automação inteligente.

**🌐 Aplicação Live:** https://aviladevops.com.br

## 📖 Resumo para IA

Este é um sistema full-stack de gestão financeira familiar que combina:
- **Frontend estático** (HTML/CSS/JS) servido pelo FastAPI
- **Backend Python** (FastAPI + SQLite) com API RESTful
- **Deploy automatizado** no Railway via Git push
- **Processamento de extratos** bancários (CSV/OFX) com extração de CPF/CNPJ
- **Autenticação simples** com roles (admin/user)

**Stack principal:** Python 3.8+, FastAPI, SQLite, Vanilla JS, Railway
**Domínio unificado:** Backend e frontend no mesmo domínio `aviladevops.com.br`

## 🚀 Funcionalidades

- **Dashboard Interativo**: Visualização de acertos e análises financeiras com gráficos
- **Importação de Extratos**: Processa arquivos CSV/OFX e extrai dados de transações
- **Detecção Automática**: Identifica CPF/CNPJ e nomes de clientes nas descrições
- **Autenticação com Roles**: Sistema de login (admin tem acesso total, users têm leitura)
- **API RESTful**: Backend FastAPI com endpoints documentados (Swagger)
- **Deploy Contínuo**: Push no GitHub → Railway faz deploy automático

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.8+**: Linguagem principal
- **FastAPI**: Framework web moderno e rápido
- **SQLite**: Banco de dados leve (persistido em volume Railway)
- **Uvicorn**: Servidor ASGI
- **Pandas**: Processamento de dados e análise de extratos
- **OFXParse**: Parser de arquivos OFX bancários

### Frontend
- **HTML5/CSS3**: Interface responsiva
- **JavaScript Vanilla**: Sem frameworks, leve e rápido
- **Fetch API**: Comunicação com backend

### DevOps
- **Railway**: Plataforma de deploy com CI/CD automático
- **Git/GitHub**: Controle de versão e trigger de deploys
- **Docker**: Containerização (via Railpack)
- **Live-Server**: Desenvolvimento local

## 📋 Pré-requisitos

- Node.js (para live-server)
- Python 3.8+
- Git

## 🔧 Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/aviladevs/avilatransportes.git
   cd avilatransportes
   ```

2. **Instale as dependências do Node.js:**
   ```bash
   npm install
   ```

3. **Instale as dependências do Python:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente (opcional):**
   - Copie `.env.example` para `.env` e ajuste conforme necessário.
   - Para produção no Railway, use as variáveis em `RAILWAY-VARS.txt`.

## 🚀 Como Executar

### Desenvolvimento Local

1. **Inicie o backend (porta 8000):**
   ```bash
   uvicorn backend.server:app --host 0.0.0.0 --port 8000
   ```

2. **Inicie o frontend (porta 3000):**
   ```bash
   npm start
   ```

3. **Acesse a aplicação:**
   - Frontend: http://localhost:3000
   - API Docs: http://localhost:8000/docs (Swagger UI)

### Autenticação Inicial

- **Usuário padrão:** `nicolasrosaab`
- **Senha:** `admin123` (mude em produção!)
- Use o endpoint `/login` para obter um token e acessar recursos protegidos.

## 🌐 Deploy no Railway (Produção)

### Configuração Automática

Este projeto está configurado para deploy contínuo no Railway:

1. **Push para GitHub** → Railway detecta automaticamente
2. **Build via Procfile** → Executa `bash start.sh`
3. **Deploy completo** → Backend + Frontend no mesmo serviço

### Variáveis de Ambiente (Railway Dashboard)

Configure em **Variables** do serviço Railway (valores em `RAILWAY-VARS.txt`):

```env
DB_PATH=/data/clientes.db
CORS_ORIGINS=https://aviladevops.com.br,http://127.0.0.1:5500
PORT=8000
```

### Volume Persistente (Recomendado)

Para persistir o banco de dados entre deploys:
- Crie um **Volume** no Railway Dashboard
- Mount path: `/data`
- Isso garante que `clientes.db` não seja perdido em redeploys

### Domínio

- **URL de Produção:** https://aviladevops.com.br
- **Health Check:** https://aviladevops.com.br/health

## 📚 Documentação da API

### Endpoints Principais

| Método | Endpoint | Descrição | Auth |
|--------|----------|-----------|------|
| GET | `/health` | Health check do servidor | Público |
| POST | `/login` | Autenticação (retorna token) | Público |
| GET | `/usuarios` | Lista usuários | Admin |
| GET | `/sync/transacoes` | Lista transações | Autenticado |
| POST | `/sync/transacoes` | Insere transações | Admin |
| POST | `/usuarios/reset` | Reseta usuários | Admin |

### Autenticação

**Header obrigatório para endpoints protegidos:**

```
Authorization: Bearer <token>
```

**Token padrão (desenvolvimento):** `admin-token`

**⚠️ Produção:** Configure JWT real e hashing de senha (bcrypt/argon2)

### Swagger UI

Acesse a documentação interativa da API:
- **Produção:** https://aviladevops.com.br/docs
- **Local:** http://localhost:8000/docs

## 🔒 Segurança

### Configurações Atuais
- **Banco de Dados:** SQLite com esquema seguro, volume persistente no Railway
- **CORS:** Restrito a `aviladevops.com.br` e localhost dev
- **Roles:** Admin (acesso total) / User (leitura limitada)
- **Static Files:** Servidos pelo FastAPI (não requer servidor separado)

### ⚠️ Para Produção Real
- [ ] Implementar JWT com expiração (pyjwt ou python-jose)
- [ ] Hashing de senha com bcrypt/argon2
- [ ] Rate limiting nos endpoints de autenticação
- [ ] HTTPS obrigatório (Railway já fornece)

## 🤝 Contribuindo

1. Fork o projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`).
4. Push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

## 📄 Licença

Este projeto é privado e propriedade da Família Rosa Ávila Barros.

## 📞 Suporte

Para suporte ou dúvidas, entre em contato com a equipe Ávila DevOps via GitHub Issues ou email.

---

**Desenvolvido com ❤️ pela Família Rosa Ávila Barros - Ávila DevOps**
