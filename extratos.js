// Sistema de Processamento de Extratos Bancários
class ExtratosManager {
    constructor() {
        this.extratoInter = [];
        this.extratoNubank = [];
        this.extratosUnificados = [];
        this.initializeData();
    }

    // Processar dados do Banco Inter (CSV)
    processarInterCSV(csvData) {
        const lines = csvData.split('\n');
        const transactions = [];
        
        // Encontrar onde começam os dados das transações
        let startIndex = -1;
        for (let i = 0; i < lines.length; i++) {
            if (lines[i].includes('Data Lançamento;Descrição;Valor;Saldo')) {
                startIndex = i + 1;
                break;
            }
        }

        if (startIndex > -1) {
            for (let i = startIndex; i < lines.length; i++) {
                const line = lines[i].trim();
                if (line && line.includes(';')) {
                    const parts = line.split(';');
                    if (parts.length >= 4) {
                        const [data, descricao, valor, saldo] = parts;
                        
                        // Converter data para formato padrão
                        const dataFormatada = this.converterDataInter(data);
                        
                        // Converter valor para número
                        const valorNum = this.converterValor(valor);
                        
                        if (dataFormatada && !isNaN(valorNum)) {
                            transactions.push({
                                data: dataFormatada,
                                descricao: descricao.replace(/"/g, ''),
                                valor: valorNum,
                                saldo: this.converterValor(saldo),
                                banco: 'Inter',
                                tipo: valorNum >= 0 ? 'Entrada' : 'Saída',
                                categoria: this.categorizarTransacao(descricao)
                            });
                        }
                    }
                }
            }
        }
        
        return transactions;
    }

    // Processar dados do Nubank (CSV)
    processarNubankCSV(csvData) {
        const lines = csvData.split('\n');
        const transactions = [];
        
        // Pular o cabeçalho
        for (let i = 1; i < lines.length; i++) {
            const line = lines[i].trim();
            if (line) {
                const parts = line.split(',');
                if (parts.length >= 4) {
                    const [data, valor, id, descricao] = parts;
                    
                    // Converter data para formato padrão
                    const dataFormatada = this.converterDataNubank(data);
                    
                    // Converter valor para número
                    const valorNum = parseFloat(valor);
                    
                    if (dataFormatada && !isNaN(valorNum)) {
                        transactions.push({
                            data: dataFormatada,
                            descricao: descricao.replace(/"/g, ''),
                            valor: valorNum,
                            banco: 'Nubank',
                            tipo: valorNum >= 0 ? 'Entrada' : 'Saída',
                            categoria: this.categorizarTransacao(descricao),
                            id: id
                        });
                    }
                }
            }
        }
        
        return transactions;
    }

    // Converter data do formato Inter (DD/MM/YYYY)
    converterDataInter(dataStr) {
        const parts = dataStr.split('/');
        if (parts.length === 3) {
            const dia = parts[0].padStart(2, '0');
            const mes = parts[1].padStart(2, '0');
            const ano = parts[2];
            return `${ano}-${mes}-${dia}`;
        }
        return null;
    }

    // Converter data do formato Nubank (DD/MM/YYYY)
    converterDataNubank(dataStr) {
        const parts = dataStr.split('/');
        if (parts.length === 3) {
            const dia = parts[0].padStart(2, '0');
            const mes = parts[1].padStart(2, '0');
            const ano = parts[2];
            return `${ano}-${mes}-${dia}`;
        }
        return null;
    }

    // Converter valor string para número
    converterValor(valorStr) {
        if (!valorStr) return 0;
        // Remove aspas e converte vírgula para ponto
        const cleanValue = valorStr.replace(/"/g, '').replace(',', '.');
        const num = parseFloat(cleanValue);
        return isNaN(num) ? 0 : num;
    }

    // Categorizar transações automaticamente
    categorizarTransacao(descricao) {
        const desc = descricao.toLowerCase();
        
        if (desc.includes('pix') || desc.includes('transferencia')) {
            if (desc.includes('enviado') || desc.includes('enviada')) {
                return 'Transferência Enviada';
            } else if (desc.includes('recebido') || desc.includes('recebida')) {
                return 'Transferência Recebida';
            }
            return 'Transferência';
        }
        
        if (desc.includes('boleto') || desc.includes('pagamento')) {
            return 'Pagamento de Conta';
        }
        
        if (desc.includes('compra') || desc.includes('débito')) {
            return 'Compra no Débito';
        }
        
        if (desc.includes('tarifa') || desc.includes('taxa')) {
            return 'Taxa/Tarifa';
        }
        
        if (desc.includes('saldo') || desc.includes('rendimento')) {
            return 'Rendimento';
        }
        
        return 'Outros';
    }

    // Unificar extratos dos dois bancos
    unificarExtratos() {
        const todos = [...this.extratoInter, ...this.extratoNubank];
        
        // Ordenar por data (mais recente primeiro)
        todos.sort((a, b) => new Date(b.data) - new Date(a.data));
        
        this.extratosUnificados = todos;
        return todos;
    }

    // Obter resumo financeiro
    obterResumo(mesAno = null) {
        let transacoes = this.extratosUnificados;
        
        if (mesAno) {
            transacoes = transacoes.filter(t => t.data.startsWith(mesAno));
        }
        
        const entradas = transacoes.filter(t => t.valor > 0);
        const saidas = transacoes.filter(t => t.valor < 0);
        
        const totalEntradas = entradas.reduce((sum, t) => sum + t.valor, 0);
        const totalSaidas = Math.abs(saidas.reduce((sum, t) => sum + t.valor, 0));
        const saldo = totalEntradas - totalSaidas;
        
        // Categorizar gastos
        const gastosPorCategoria = {};
        saidas.forEach(t => {
            if (!gastosPorCategoria[t.categoria]) {
                gastosPorCategoria[t.categoria] = 0;
            }
            gastosPorCategoria[t.categoria] += Math.abs(t.valor);
        });
        
        return {
            totalEntradas: totalEntradas.toFixed(2),
            totalSaidas: totalSaidas.toFixed(2),
            saldo: saldo.toFixed(2),
            quantidadeTransacoes: transacoes.length,
            gastosPorCategoria,
            periodo: mesAno || 'Todos os períodos'
        };
    }

    // Filtrar transações por critérios
    filtrarTransacoes(filtros = {}) {
        let resultado = this.extratosUnificados;
        
        if (filtros.banco) {
            resultado = resultado.filter(t => t.banco === filtros.banco);
        }
        
        if (filtros.categoria) {
            resultado = resultado.filter(t => t.categoria === filtros.categoria);
        }
        
        if (filtros.tipo) {
            resultado = resultado.filter(t => t.tipo === filtros.tipo);
        }
        
        if (filtros.dataInicio && filtros.dataFim) {
            resultado = resultado.filter(t => 
                t.data >= filtros.dataInicio && t.data <= filtros.dataFim
            );
        }
        
        if (filtros.valorMinimo) {
            resultado = resultado.filter(t => Math.abs(t.valor) >= filtros.valorMinimo);
        }
        
        if (filtros.descricao) {
            const termo = filtros.descricao.toLowerCase();
            resultado = resultado.filter(t => 
                t.descricao.toLowerCase().includes(termo)
            );
        }
        
        return resultado;
    }

    // Exportar dados para análise
    exportarParaCSV() {
        const headers = ['Data', 'Banco', 'Descrição', 'Valor', 'Tipo', 'Categoria'];
        const csvContent = [
            headers.join(','),
            ...this.extratosUnificados.map(t => [
                t.data,
                t.banco,
                `"${t.descricao}"`,
                t.valor,
                t.tipo,
                t.categoria
            ].join(','))
        ].join('\n');
        
        return csvContent;
    }

    // Inicializar com dados de exemplo (para demonstração)
    initializeData() {
        // Aqui você pode carregar dados salvos anteriormente
        this.extratoInter = [];
        this.extratoNubank = [];
        this.extratosUnificados = [];
    }

    // Carregar dados dos arquivos CSV
    carregarExtratos(interCSV, nubankCSV) {
        if (interCSV) {
            this.extratoInter = this.processarInterCSV(interCSV);
        }
        
        if (nubankCSV) {
            this.extratoNubank = this.processarNubankCSV(nubankCSV);
        }
        
        this.unificarExtratos();
        return this.extratosUnificados;
    }

    // Obter transações suspeitas ou interessantes
    obterTransacoesSuspeitas() {
        const suspeitas = [];
        
        // Transações de valor muito alto
        const transacoesAltas = this.extratosUnificados.filter(t => 
            Math.abs(t.valor) > 5000
        );
        
        // Múltiplas transações no mesmo dia para a mesma pessoa/empresa
        const transacoesPorDia = {};
        this.extratosUnificados.forEach(t => {
            const chave = `${t.data}-${t.descricao.substring(0, 30)}`;
            if (!transacoesPorDia[chave]) {
                transacoesPorDia[chave] = [];
            }
            transacoesPorDia[chave].push(t);
        });
        
        const transacoesRepetidas = Object.values(transacoesPorDia)
            .filter(grupo => grupo.length > 3);
        
        return {
            valoresAltos: transacoesAltas,
            transacoesRepetidas: transacoesRepetidas.flat()
        };
    }
}

// Instância global do gerenciador
const extratosManager = new ExtratosManager();