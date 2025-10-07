# Conversão de Extratos (CSV/OFX) para SQLite

Este utilitário cria um banco `clientes.db` a partir de arquivos `.csv` e `.ofx` (Nubank, Inter e OFX padrão).

## Requisitos

- Python 3.10+
- Pip

Instale as dependências (Windows PowerShell):

```powershell
python -m pip install -r requirements.txt
```

## Como usar

Na raiz do projeto:

```powershell
# Descobrir automaticamente CSV/OFX em toda a pasta
python converter_ofx_sqlite.py --input .

# Ou passando padrões de arquivo
python converter_ofx_sqlite.py --input NU_*.ofx Extrato-*.ofx *.csv
```

Saída:
- Banco `clientes.db`
- Tabela `transacoes` consolidada com colunas: data, cnpj_cpf, cliente, valor, descricao
- Uma tabela por cliente: `cliente_<cnpj_cpf>`

## Observações
- Deduplicação por (data, valor, descricao)
- Datas normalizadas para `YYYY-MM-DD`
- Valores convertidos para `float` considerando formatos BR/US
- Extração de CPF/CNPJ e limpeza do nome a partir da descrição
