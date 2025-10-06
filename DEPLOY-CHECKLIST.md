# 🚀 CHECKLIST PARA DEPLOY - avilatransportes.com.br

## ✅ **Arquivos Prontos para Upload:**

### 📁 **Estrutura Completa:**
```
avilatransportes.com.br/acertos/
├── index.html              ✅ Página inicial
├── login.html               ✅ Sistema de login  
├── acertos.html             ✅ Dashboard principal
├── analise.html             ✅ Ferramenta análise
├── extratos.js              ✅ Motor processamento
├── dados-exemplo.js         ✅ Dados reais família
├── .htaccess                ✅ Configurações servidor
├── package.json             ✅ Metadados projeto
└── README.md                ✅ Documentação
```

## 🔧 **Configurações do Servidor:**

### **1. Hospedagem Recomendada:**
- ✅ **Apache/Nginx** com suporte a HTML5
- ✅ **HTTPS obrigatório** (certificado SSL)
- ✅ **PHP não necessário** (100% frontend)
- ✅ **Espaço:** Mínimo 10MB

### **2. Upload via FTP/cPanel:**
```bash
# Estrutura no servidor:
/public_html/acertos/
├── todos os arquivos listados acima
```

### **3. URLs de Acesso:**
- **Principal:** https://avilatransportes.com.br/acertos/
- **Login:** https://avilatransportes.com.br/acertos/login.html
- **Dashboard:** https://avilatransportes.com.br/acertos/acertos.html

## 🔒 **SEGURANÇA - AÇÃO NECESSÁRIA:**

### ⚠️ **ALTERAR SENHAS ANTES DO DEPLOY:**

Editar arquivo: `login.html` (linhas 142-157)
```javascript
// ALTERAR ESTAS SENHAS:
const familiaMembers = {
    'sueli': {
        nome: 'Sueli Menezes Rosa',
        senha: 'NOVA_SENHA_SEGURA_2024',  // ← ALTERAR
        role: 'administrador'
    },
    'renato': {
        nome: 'Renato Avila Barros', 
        senha: 'NOVA_SENHA_SEGURA_2024',  // ← ALTERAR
        role: 'membro'
    },
    // ... alterar todas as senhas
};
```

## 📱 **Funcionalidades Prontas:**

### ✅ **Sistema Completo:**
- 👥 **Login familiar** com controle de acesso
- 💰 **Dívidas reais** da Ávila Transportes carregadas:
  - Sueli: R$ 11.300,00
  - Renato: R$ 14.647,84  
  - Guilherme: R$ 1.400,00 (+ R$ 1.685 recebido)
- 📊 **Dashboard interativo** com filtros
- ➕ **Adicionar dívidas/recebimentos**
- 📎 **Upload de comprovantes** (PDF/imagem)
- 📱 **Responsivo** (mobile/desktop)

### ✅ **Dados Reais Incluídos:**
- **PIX Guilherme:** R$ 1.685,00 (29/09/2025)
- **Parcelas cartão:** 6 pendentes de R$ 1.498,96
- **Manutenção Strada:** R$ 6.680,00 (dividido)
- **Chat WhatsApp:** Todas as informações processadas

## 🎯 **Processo de Deploy:**

### **1. Preparação Final:**
```bash
# 1. Alterar senhas no login.html
# 2. Testar localmente
# 3. Fazer upload via FTP/cPanel
# 4. Configurar SSL
# 5. Testar no domínio
```

### **2. Verificação Pós-Deploy:**
- [ ] Acessar https://avilatransportes.com.br/acertos/
- [ ] Testar login de cada membro da família
- [ ] Verificar carregamento dos dados
- [ ] Testar upload de arquivos
- [ ] Verificar responsividade mobile

### **3. Configuração DNS (se necessário):**
```
# Se usar subdomínio:
acertos.avilatransportes.com.br → CNAME → avilatransportes.com.br
```

## 📞 **Acesso da Família:**

### **URLs para compartilhar:**
- **Principal:** https://avilatransportes.com.br/acertos/
- **Direto login:** https://avilatransportes.com.br/acertos/login.html

### **Credenciais (APÓS ALTERAR SENHAS):**
- **Sueli Menezes Rosa:** sueli / [nova_senha]
- **Renato Avila Barros:** renato / [nova_senha]  
- **Guilherme Rosa Avila Barros:** guilherme / [nova_senha]
- **Lara Rosa Avila Barros:** lara / [nova_senha]

---

## ✅ **SISTEMA 100% PRONTO PARA PRODUÇÃO!**

**Próximos passos:**
1. ⚠️ **ALTERAR SENHAS** 
2. 📤 **Upload para servidor**
3. 🔒 **Configurar HTTPS**
4. 🎉 **Compartilhar com família**