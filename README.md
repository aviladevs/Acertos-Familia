# Sistema de Acertos Família - Ávila DevOps

Um sistema completo para controle de acertos financeiros da família, desenvolvido pela equipe Ávila DevOps. Gerencia transações, análises financeiras e integra com APIs bancárias para automação.

## 🚀 Funcionalidades

- **Dashboard Interativo**: Visualização de acertos e análises financeiras.
- **Sincronização de Transações**: Integração com bancos para importação automática de dados.
- **Autenticação Segura**: Sistema de login com roles de usuário (admin/usuário).
- **Análise de Extratos**: Ferramentas para processar e analisar extratos bancários (CSV, OFX, PDF).
- **API RESTful**: Backend em Python/FastAPI para operações CRUD e integração.
- **Deploy Automatizado**: Configurado para deploy no Railway com domínio personalizado.

## 🛠️ Tecnologias Utilizadas

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python, FastAPI, SQLite
- **Deploy**: Railway, GitHub Pages (fallback)
- **Outras**: Live-Server para desenvolvimento local, Pandas para análise de dados

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

## 🌐 Deploy no Railway

1. **Conecte o repositório ao Railway.**
2. **Configure as variáveis de ambiente** em `RAILWAY-VARS.txt` no dashboard do Railway.
3. **Defina o domínio personalizado:** `avilatransportes.com.br` no painel de domínios do serviço.
4. **Deploy automático:** O Railway detecta pushes no GitHub e faz deploy.

- **URL de Produção:** https://avilatransportes.com.br

## 📚 Documentação da API

### Endpoints Principais

- **GET /health** - Verifica status do servidor.
- **POST /login** - Autenticação de usuário (retorna token).
- **GET /usuarios** - Lista usuários (apenas admin).
- **GET /sync/transacoes** - Lista transações (autenticado).
- **POST /sync/transacoes** - Insere transações (apenas admin).

### Autenticação

- Use o header `Authorization: Bearer <token>` para endpoints protegidos.
- Token padrão para admin: `admin-token` (configure em produção).

## 🔒 Segurança

- **Banco de Dados:** SQLite com esquema seguro.
- **CORS:** Configurado para domínios específicos.
- **Roles:** Admin tem acesso total; usuários comuns têm leitura limitada.
- **Nota:** Em produção, use hashing de senha (e.g., bcrypt) e JWT para tokens.

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
