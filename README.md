# 👨‍👩‍👧‍👦 Sistema de Acertos Família Rosa Avila Barros

![Uptime](https://github.com/aviladevs/avilatransportes/actions/workflows/uptime.yml/badge.svg?branch=main)

Sistema completo para gestão de acertos familiares com controle de acesso e análise financeira.

## 🏠 Estrutura do Sistema

### Páginas Principais:

1. **`index.html`** - Landing page principal
   - Informações sobre interdição legal
   - Navegação para outras funcionalidades

2. **`login.html`** - Página de acesso da família
   - Login seguro para membros autorizados
   - Controle de acesso por credenciais

3. **`acertos.html`** - Dashboard familiar (requer login)
   - Visualização dos dados financeiros unificados
   - Análise completa dos extratos bancários
   - Filtros e exportação de dados

4. **`analise.html`** - Ferramenta de análise técnica
   - Upload de extratos bancários
   - Processamento e unificação de dados
   - Análise detalhada para administradores

### Arquivos de Suporte:

- **`extratos.js`** - Motor de processamento financeiro
- **`dados-exemplo.js`** - Dados de exemplo para demonstração

## 👥 Membros Autorizados

O sistema permite acesso aos seguintes membros da família:

| Nome | Usuário | Senha | Função |
|------|---------|-------|---------|
| Sueli Menezes Rosa | `sueli` | `sueli2024` | Administrador |
| Renato Avila Barros | `renato` | `renato2024` | Membro |
| Guilherme Rosa Avila Barros | `guilherme` | `guilherme2024` | Membro |
| Lara Rosa Avila Barros | `lara` | `lara2024` | Membro |

## 🚀 Como Usar

### Para Membros da Família:

1. **Acesso ao Sistema:**
   - Abra `index.html` no navegador
   - Clique em "👥 Acertos Família"
   - Faça login com suas credenciais

2. **Visualizar Dados:**
   - O sistema carrega automaticamente os dados financeiros
   - Use os filtros para análises específicas
   - Exporte relatórios em CSV

### Para Administradores:

1. **Carregar Novos Dados:**
   - Acesse `analise.html` diretamente
   - Faça upload dos extratos do Banco Inter e Nubank
   - Processe e analise os dados
   - Os dados processados ficam disponíveis no sistema familiar

## 💰 Funcionalidades Financeiras

### Bancos Suportados:
- **Banco Inter** - Processamento de CSV
- **Nubank** - Processamento de CSV

### Análises Disponíveis:
- ✅ Total de entradas e saídas
- ✅ Saldo líquido familiar
- ✅ Categorização automática de transações
- ✅ Filtros por data, valor, categoria, banco
- ✅ Busca por descrição
- ✅ Exportação para CSV

### Categorias de Transações:
- 🍽️ Alimentação
- 🚗 Transporte
- 🏥 Saúde
- 📚 Educação
- 🎮 Lazer
- 💸 Transferência Recebida
- 📦 Outros

## 🔒 Segurança

- **Autenticação:** Sistema de login por credenciais familiares
- **Sessão:** Controle de sessão por navegador
- **Acesso:** Dados financeiros protegidos por login
- **Logout:** Botão de saída segura

## 📱 Responsividade

O sistema é totalmente responsivo e funciona em:
- 💻 Computadores (Desktop)
- 📱 Tablets
- 📱 Smartphones

## 🔧 Tecnologias Utilizadas

- **HTML5** - Estrutura das páginas
- **CSS3** - Design responsivo e moderno
- **JavaScript ES6+** - Lógica de negócio e processamento
- **File API** - Upload e processamento de arquivos
- **SessionStorage** - Gerenciamento de sessão

## 🌐 Domínio, HTTPS e Monitoramento

### Enforce HTTPS (GitHub Pages)

1. Repositório no GitHub → Settings → Pages
2. Custom domain: confirme `avilatransportes.com.br` (o arquivo `CNAME` já está no repositório)
3. Ative “Enforce HTTPS” (após o certificado ser provisionado pelo GitHub)

Camada extra no código:
- Todas as páginas incluem `force-https.js` que redireciona automaticamente para HTTPS (exceto localhost/file) e meta `Content-Security-Policy: upgrade-insecure-requests`.

### DNS (resumo)

- Aponte o domínio `avilatransportes.com.br` para GitHub Pages com os CNAMEs sugeridos pelo GitHub (normalmente `username.github.io.`)
- Mantenha o arquivo `CNAME` com `avilatransportes.com.br` na raiz do repositório

### Monitoramento de Uptime (GitHub Actions)

Workflow: `.github/workflows/uptime.yml`
- Agenda: a cada 30 minutos (ou manual via Actions)
- URLs verificadas:
   - https://avilatransportes.com.br
   - https://www.avilatransportes.com.br
   - https://aviladevs.github.io/avilatransportes/
- Em caso de falha: abre automaticamente um Issue com detalhes

Notificações opcionais:
- Slack: crie um Incoming Webhook e adicione o secret no repo
   - Settings → Secrets and variables → Actions → New repository secret
   - Nome: `SLACK_WEBHOOK_URL` | Valor: URL do webhook
- Telegram: (opcional) crie um bot (BotFather) e obtenha `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID`
   - Adicione os secrets no repo e podemos ativar o passo (está comentado no workflow)
- E-mail: podemos adicionar futuramente via SMTP (SendGrid/Mailgun/outros) sob demanda

Badge de status:
- Já incluso no topo deste README (status do workflow `uptime.yml` na branch `main`).

## 📋 Dados de Exemplo

O sistema inclui dados de exemplo baseados nos extratos reais fornecidos:
- Transações do Banco Inter
- Transações do Nubank
- Período: Dados históricos familiares
- Total: 3554+ transações processadas

## 🎯 Acesso Rápido

### Para começar agora:
1. Abra `index.html`
2. Clique em "👥 Acertos Família"
3. Use as credenciais de qualquer membro listado acima
4. Explore os dados financeiros da família

### Para análise técnica:
1. Abra `analise.html` diretamente
2. Clique em "🎯 Carregar Dados de Exemplo"
3. Ou faça upload dos seus próprios extratos CSV

## 💡 Dicas de Uso

- **Filtros:** Use múltiplos filtros combinados para análises específicas
- **Exportação:** Exporte dados filtrados para análise externa
- **Mobile:** O sistema funciona perfeitamente em celulares
- **Atualizações:** Dados ficam salvos na sessão do navegador

## 📞 Suporte

Para dúvidas ou problemas:
- Sistema desenvolvido para uso familiar
- Interface intuitiva e auto-explicativa
- Dados de exemplo disponíveis para teste

---

**Sistema de Acertos Família Rosa Avila Barros**  
*Desenvolvido com ❤️ para organização financeira familiar*