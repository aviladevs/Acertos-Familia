# 👥 Como Adicionar Novos Usuários

## 📋 Passos para Adicionar um Novo Usuário

### 1. **Editar o arquivo `login.html`**

Encontre a seção `familiaMembers` (linha ~235) e adicione o novo usuário:

```javascript
const familiaMembers = {
    // ... usuários existentes ...
    'chaveusuario': {
        nome: 'Nome Completo do Usuário',
        senha: 'senhadeseguranca',
        role: 'membro'  // ou 'administrador'
    }
};
```

### 2. **Adicionar no dropdown de seleção**

Na mesma página, encontre o `<select id="membro">` (linha ~203) e adicione:

```html
<option value="chaveusuario">Nome Completo do Usuário</option>
```

## 🔧 Exemplo Prático

Para adicionar o usuário "Maria Silva":

### No JavaScript:
```javascript
'maria': {
    nome: 'Maria Silva',
    senha: 'maria123',
    role: 'membro'
}
```

### No HTML:
```html
<option value="maria">Maria Silva</option>
```

## 👑 Tipos de Usuário

### **Administrador**
- `role: 'administrador'`
- Acesso total ao sistema
- Pode ver todos os dados

### **Membro**
- `role: 'membro'`
- Acesso padrão
- Funcionalidades básicas

## 🔐 Dicas de Segurança

1. **Senhas Seguras**: Use senhas com pelo menos 8 caracteres
2. **Chaves Únicas**: Cada usuário deve ter uma chave única (sem espaços, minúsculas)
3. **Nomes Claros**: Use nomes completos para identificação

## 📝 Template para Novo Usuário

```javascript
// 1. Adicione em familiaMembers:
'chave_do_usuario': {
    nome: 'Nome Completo',
    senha: 'senha_segura_123',
    role: 'membro'
},

// 2. Adicione no <select>:
<option value="chave_do_usuario">Nome Completo</option>
```

## ✅ Exemplo Completado

Já adicionei um usuário exemplo para você:

- **Chave**: `novousuario`
- **Nome**: `Nome do Novo Usuário`
- **Senha**: `senhadonovousuario`
- **Role**: `membro`

### Para personalizar:
1. Mude `'novousuario'` para a chave desejada
2. Altere `'Nome do Novo Usuário'` para o nome real
3. Troque `'senhadonovousuario'` por uma senha segura
4. Escolha `'membro'` ou `'administrador'` para o role

## 🚀 Testando

1. Salve o arquivo `login.html`
2. Abra o site
3. Vá para a página de login
4. Teste o novo usuário

O novo usuário já está funcionando e pode fazer login no sistema! 🎉