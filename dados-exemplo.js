// Dados reais dos acertos da família - Dívidas da Ávila Transportes
function carregarDadosAcertos() {
    const dadosAcertos = [
        // Dívidas com a Mãe (Sueli Menezes Rosa) - TOTAL: R$ 11.300,00
        {
            id: 'div001',
            data: '2025-01-15',
            banco: 'Dívida Familiar',
            descricao: 'Empréstimo para Ávila Transportes - Parte 1',
            valor: -4500.00,
            categoria: 'Empréstimo Familiar',
            devedor: 'Ávila Transportes (Nícolas)',
            credor: 'Sueli Menezes Rosa',
            status: 'Pendente',
            observacao: 'Primeira parte da dívida total de R$ 11.300',
            vencimento: '2025-12-31'
        },
        {
            id: 'div002',
            data: '2025-02-10',
            banco: 'Dívida Familiar',
            descricao: 'Manutenção Strada - Gastos Sueli',
            valor: -6800.00,
            categoria: 'Manutenção Veículo',
            devedor: 'Ávila Transportes (Nícolas)',
            credor: 'Sueli Menezes Rosa',
            status: 'Pendente',
            observacao: 'Manutenção da pick-up do pai que está com a empresa',
            vencimento: '2025-12-31'
        },
        
        // Dívidas com o Pai (Renato Avila Barros)
        {
            id: 'pag001',
            data: '2025-08-28',
            banco: 'Cartão Latam',
            descricao: 'Pagamento cartão Guilherme - Parcela 5/12 Despachante',
            valor: -1498.96,
            categoria: 'Despachante',
            devedor: 'Ávila Transportes (Nícolas)',
            credor: 'Renato Avila Barros',
            status: 'Pago',
            observacao: 'Despachante Fernando - Liberação caminhão preso',
            vencimento: '2025-08-28'
        },
        {
            id: 'rec001',
            data: '2025-09-29',
            banco: 'PIX',
            descricao: 'PIX recebido de Renato Avila Barros - R$ 1.685,00',
            valor: 1685.00,
            categoria: 'Pagamento Recebido',
            devedor: 'Renato Avila Barros',
            credor: 'Guilherme Rosa Avila Barros',
            status: 'Pago',
            observacao: 'Comprovante: Quinta, 29/09/2025 às 09:19 - Bco Do Brasil S A',
            vencimento: '2025-09-29',
            comprovante: 'Comprovante_29-09-2025_191417.pdf'
        }
    ];

    console.log('Dados de acertos carregados:', dadosAcertos.length, 'registros');
    return dadosAcertos;
}

// Função para carregar dados de exemplo (manter compatibilidade)
function carregarDadosExemplo() {
    return carregarDadosAcertos();
} 
Conta ;431913919
Período ;01/01/2025 a 06/10/2025
Saldo: ;0,00

Data Lançamento;Descrição;Valor;Saldo
15/03/2025;Pix recebido: "Cp :00000000-RENATO AVILA BARROS";600,00;600,00
16/03/2025;Pix enviado: "Cp :18236120-Alceu Rodrigues Neto";-400,00;200,00
17/03/2025;Pix recebido: "00019 219817430 LZP COMERCIAL LTDA";60,00;260,00
20/03/2025;Pix recebido: "Cp :90400888-NARDINI AGROINDUSTRIAL LTDA";551,89;4,89
31/03/2025;Transferencia recebida: "341 9 147786 NARDINI AGROINDUSTRIAL LTDA";220,00;-70,00
04/04/2025;Boleto de cobranca recebido: "112/90265349673";304,00;-0,00
10/04/2025;Boleto de cobranca recebido: "112/90272470553";633,43;1.266,06
10/04/2025;Pix enviado: "Cp :18236120-Avila Transportes Intermunicipal LTDA";-3.313,70;-2.047,64
10/04/2025;Pix recebido: "Cp :90400888-NARDINI AGROINDUSTRIAL LTDA";3.580,00;989,02
11/04/2025;Pix enviado: "Cp :54403563-M4 PRODUTOS E SERVICOS LTDA";-40,00;305,30
14/04/2025;Tarifa liquidacao de boleto: "Tarifa boleto pagamento via Cod Barras";-2,49;-24,72
22/04/2025;Pix recebido: "Cp :90400888-NARDINI AGROINDUSTRIAL LTDA";818,18;-0,00
25/04/2025;Boleto de cobranca recebido: "112/90279345931";205,00;-120,00
28/04/2025;Pix enviado: "Cp :18236120-Avila Transportes Intermunicipal LTDA";-699,02;-699,02
29/04/2025;Boleto de cobranca recebido: "112/90272469993";700,76;700,76
30/04/2025;Pix enviado: "Cp :18236120-Avila Transportes Intermunicipal LTDA";-6.343,67;-5.642,91
30/04/2025;Pix enviado: "Cp :90400888-Polartech Mirassol Ar Condicionado LTDA";-1.350,00;-2.227,03
30/04/2025;Pix enviado: "Cp :02466552-BSOFT INTERNETWORKS";-2.110,51;-2.170,13
02/05/2025;Boleto de cobranca recebido: "112/90279345352";642,78;642,78
05/05/2025;Pix enviado: "Cp :10573521-Igor Melo de Lucena";-91,16;-90,98
05/05/2025;Pix enviado: "Cp :30385259-KUPFY";-19,99;22,03
12/05/2025;Pix enviado: "Cp :18236120-Avila Transportes Intermunicipal LTDA";-370,00;-369,97
12/05/2025;Transferencia recebida: "341 9 147786 NARDINI AGROINDUSTRIAL LTDA";1.098,81;-370,34
15/05/2025;Pix enviado: "Cp :08561701-Sol Cargas Transportes Multimodal LTDA";-169,16;-354,16
15/05/2025;Pix enviado: "Cp :10573521-LALAMOVE TECNOLOGIA BRASIL LTDA";-50,00;-59,21
16/05/2025;Pix enviado: "Cp :18236120-Avila Transportes Intermunicipal LTDA";-268,00;476,06
19/05/2025;Pix enviado: "Cp :10573521-LALAMOVE TECNOLOGIA BRASIL LTDA";-70,00;-96,63
20/05/2025;Pix recebido: "Cp :90400888-NARDINI AGROINDUSTRIAL LTDA";630,06;60,00
21/05/2025;Boleto de cobranca recebido: "112/90308067506";1.110,00;60,00
22/05/2025;Pix recebido: "Cp :60701190-TIM S A";3,00;0,51
24/05/2025;Pix recebido: "Cp :18236120-AVILA TRANSPORTES INTERMUNICIPAL LTDA";202,41;202,92
25/05/2025;Pix enviado: "Cp :90400888-Danilo Fernandes Saraiva";-111,44;91,48
25/05/2025;Pix enviado: "Cp :21018182-Uber";-11,58;79,90
25/05/2025;Pix enviado: "Cp :90400888-RAIA DROGASIL SA";-29,66;14,69
26/05/2025;Pix enviado: "Cp :60701190-Bravo City Hotel Sao Jose do Rio Preto LTDA";-156,00;-156,00
26/05/2025;Pix recebido: "Cp :54037916-VIP VINHOS - EIRELI";370,00;-72,14
27/05/2025;Pix enviado: "Cp :01027058-WILLIAM LOPES DA SILVARESTAURAN";-43,90;51,93
27/05/2025;Pix enviado: "Cp :90400888-RAIA DROGASIL SA";-4,06;35,60
28/05/2025;Boleto de cobranca recebido: "112/90279345501";133,12;-112,78
29/05/2025;Pix enviado: "Cp :22896431-Adney Leite da Silva";-250,00;-249,04
29/05/2025;Pix enviado: "Cp :03065046-Cavaleiros de Aco Noroeste Paulista 417";-500,00;-749,04
30/05/2025;Pix enviado: "Cp :90400888-RAIA DROGASIL SA";-31,67;75,31
30/05/2025;Pix enviado: "Cp :21018182-Uber";-19,53;45,78
31/05/2025;Pix recebido: "Cp :31872495-MATHEUS TROVATTI";495,00;-67,46
01/06/2025;Pix recebido: "Cp :00000000-ADRIANO A O CORRENTE";60,00;68,00
02/06/2025;Pix recebido: "Cp :60701190-TIM S A";3,00;71,00
02/06/2025;Pix enviado: "Cp :54403563-M4 PRODUTOS E SERVICOS LTDA";-40,00;31,00
03/06/2025;Pix enviado: "Cp :90400888-COMPANHIA PAULISTA DE FORCA E LUZ";-105,49;152,69
03/06/2025;Pix enviado: "Cp :90400888-TELEFONICA BRASIL S A";-496,10;-570,99
04/06/2025;Pix enviado: "Cp :90400888-CABRAL ESPETOS E PASTEIS";-69,96;0,05
05/06/2025;Pix enviado: "Cp :18236120-Sueli Menezes Rosa";-2.500,00;-2.537,63
05/06/2025;Pix enviado: "Cp :18236120-Luiza Silva de Oliveira";-650,00;-3.187,63
06/06/2025;Pix enviado: "Cp :60701190-Nayra Kelly M Rodero Saraiva";-1.000,00;-905,49
07/06/2025;Pix enviado: "Cp :90400888-Natalia Josy Alves de Oliveira";-1.440,00;-1.925,21
07/06/2025;Pix recebido: "Cp :18236120-Sueli Menezes Rosa";2.500,00;574,79
08/06/2025;Pix enviado: "Cp :90400888-VALU LANCHES";-91,19;454,50
09/06/2025;Pix enviado: "Cp :09089356-NIC BR";-40,00;-34,66
10/06/2025;Pix recebido: "Cp :90400888-NARDINI AGROINDUSTRIAL LTDA";1.324,32;1.721,87
11/06/2025;Pix enviado: "Cp :08561701-Sol Cargas Transportes Multimodal LTDA";-42,46;1.652,41`,

    nubank: `Data,Valor,Identificador,Descrição
02/01/2025,120.00,6776a1f3-ec94-4ad1-b200-60623cd514a2,Transferência recebida pelo Pix - VIVIANE E SILVA ROTIROTI
02/01/2025,-107.94,6776a60a-0c57-4bec-a148-275c34408a8d,Compra no débito - Muffato Sjrp
02/01/2025,-5.99,6776a8c2-b69b-45a9-a3d9-9cc2c6cd9a6f,Compra no débito - Farmacia Paulista
02/01/2025,50.00,6776c835-f0c8-4d2d-9473-7881cf81639f,Transferência recebida pelo Pix - Agro Vallen Pecas Agricolas Ltda
02/01/2025,-43.10,6776d894-a62c-4891-9a02-31a2542d04b2,Compra no débito - Beato Coffe
02/01/2025,954.00,6776ff10-eccb-4f59-8be3-354f9744c421,Transferência Recebida - ALAN BELUZI 38875959803
02/01/2025,280.00,6777003f-75f8-40e4-9dad-bc9a149049b5,Transferência recebida pelo Pix - DV4 do Brasil
02/01/2025,-800.00,677701fc-46dd-40cb-b9ae-d35950add4c8,Transferência enviada pelo Pix - Lh Transporte e Logistica
02/01/2025,-15.00,677702b7-e9d9-43d2-b65a-178198489a9c,Transferência enviada pelo Pix - JOAO BATISTA BISPO
02/01/2025,-35.00,67770492-8f66-4d47-a457-547ff606bf4f,Compra no débito - Mp *Lanchonetetie
02/01/2025,-300.00,67770747-4ce6-48ab-bd74-90674a614e71,Transferência enviada pelo Pix - Marcio Candido Rosa
02/01/2025,-9.60,67770d31-4b20-4b06-8cad-afd9f20bec9b,Transferência enviada pelo Pix - TRANSBRASILIANA CONCESSIONARIA DE RODOVIA SA
02/01/2025,60.00,67772699-be32-4740-b755-e2fba9fe97f9,Transferência recebida pelo Pix - ANGELA BELUZI DE FREITAS
03/01/2025,149.99,67781575-d5ae-4954-9403-566172e326fb,Transferência recebida pelo Pix - M. D. INDUSTRIA QUIMICA LTDA - EPP
03/01/2025,52.00,6778192d-caec-4fde-a35f-de8005dfc470,Transferência recebida pelo Pix - FABRO ELETRICA E AR CONDICIONADO AUTOMOTIVO LTDA
03/01/2025,-180.00,6778199a-f589-40b3-a07c-949d2955d71d,Transferência enviada pelo Pix - João Vitor Parise
03/01/2025,48.00,67783072-c3c2-4817-9009-32ffff828a04,Transferência recebida pelo Pix - TRACKMAX COMERCIO DE PECAS E SERVICOS LTDA
03/01/2025,-73.00,67783609-3fc7-4dec-852f-39b12fe20464,Transferência enviada pelo Pix - Drogaria Lealdade Amizade Ltda Me
06/01/2025,90.00,677bd7e0-366e-4754-b2e1-3bfdfcfa4f7a,Transferência recebida pelo Pix - MASTER PRINT 017 LTDA
06/01/2025,60.00,677c241a-5d7f-4b0c-ac13-03d2cb05080e,Transferência recebida pelo Pix - ROBERTO CARLOS BERTOLOSSI
06/01/2025,-150.00,677c280a-a0d0-48e3-991f-7065e0a674e1,Transferência enviada pelo Pix - Marcio Candido Rosa
06/01/2025,80.00,677c3230-168c-4f2a-88ea-a3a6062b230c,Transferência Recebida - Sonia Perpetua Thomas
06/01/2025,410.00,677c4cb1-bce4-f27-a0bb-1ab55638e77b,Transferência recebida pelo Pix - DOMENICO E RAVELLI &amp; CIA LTDA
06/01/2025,-490.00,677c5127-0e5c-44de-b9d3-79af290a34f9,Transferência enviada pelo Pix - Sl Transportes e Representacoes Ltda
07/01/2025,60.00,677d1e8a-2afd-4f8d-97f1-ced1752a1767,Transferência recebida pelo Pix - MAQUINAS LEONE
07/01/2025,-60.00,677d2174-0af5-45ea-8e60-ca26893e941c,Transferência enviada pelo Pix - João Vitor Parise
07/01/2025,80.00,677d217f-6747-4900-8515-77b3fef00c66,Transferência recebida pelo Pix - 51.500.508 NELSON AP DE NADAI
07/01/2025,-80.00,677d2f70-64bb-4fca-bff1-74b0e8cbddc7,Transferência enviada pelo Pix - Marcio Candido Rosa
07/01/2025,120.00,677d3b2b-024d-447b-9f11-945a8a8b1dd0,Transferência recebida pelo Pix - BR LUX LTDA
07/01/2025,60.00,677d4138-e921-46f4-8ead-aaaba6d1a714,Transferência recebida pelo Pix - INTERIOR INTERIORES LTDA
07/01/2025,258.00,677d453d-ac05-4d65-a1eb-9f8bc147c982,Transferência recebida pelo Pix - DAILSON MARTINS DE SOUZA
07/01/2025,-260.00,677d566b-1934-4266-82ca-049e6d7d9455,Transferência enviada pelo Pix - 54454130 Mariana Flavia Polizel
07/01/2025,-178.00,677d5e9c-9ef0-4492-8043-b23fdf7a1c44,Transferência enviada pelo Pix - João Vitor Parise
07/01/2025,4308.51,677d636c-56a0-414c-a982-183f6fb870a8,Transferência recebida pelo Pix - PORTOEXPRESS LOGISTICA EIRELI
07/01/2025,-40.00,677d6913-54ad-480f-b112-db0d4efaf14d,Transferência enviada pelo Pix - VINICIUS QUILES SUETH INFORMATICA
07/01/2025,-33.50,677d6e69-283a-4cc7-8d64-0ada636ed3a1,Compra no débito - Jubernal Salgados
07/01/2025,-215.42,677d716e-e947-49c6-9457-8c8f6cc2a740,Transferência enviada pelo Pix - FERNANDO GAMARANO DE OLIVEIRA
07/01/2025,-200.00,677d72af-b695-4b11-8953-10e341a253be,Transferência enviada pelo Pix - Marcio Candido Rosa
07/01/2025,-1754.80,677d7304-89d1-4c2f-b596-cba514503de6,Transferência enviada pelo Pix - Fabiano Bruno Campos 21892138867
07/01/2025,-276.08,677d73c9-cb6d-4c14-b53e-819f9f9261cd,Pagamento de boleto efetuado - ALEXANDRE VIGANO ALARMES
07/01/2025,-436.14,677d740a-4e5c-4f2f-a874-700342600fe5,Pagamento de boleto efetuado - TRANSPORTADORA GLI LTDA
07/01/2025,-139.90,677d749f-6268-4680-859e-7f7b8b331c11,Pagamento de boleto efetuado - FSIST
07/01/2025,-215.96,677d74dc-6e4b-466d-9dd0-c7e20f08e3ff,Pagamento de boleto efetuado - ZANARDI TRANSPORTES LTDA
07/01/2025,538.50,677d74fc-fe1a-47f8-b61c-e7b2b88caf23,Transferência recebida pelo Pix - PROLINK INDUSTRIA QUIMICA LTDA
07/01/2025,60.00,677d7558-1366-4755-8393-4402ba872b45,Transferência recebida pelo Pix - Melisa Ar Condicionado Ltda
07/01/2025,130.00,677d782e-ff6b-4ae7-b711-96cccf741bda,Transferência recebida pelo Pix - VANDERCLAITON P CORREA
07/01/2025,238.00,677d874c-8bbd-4779-9c92-af861ed5f003,Transferência recebida pelo Pix - BUFALO COMERCIO DE VIDROS LTDA
07/01/2025,-1500.00,677d9587-2e22-49cc-8d4a-a619189ca3b4,Transferência enviada pelo Pix - Flavia Cristina Ferrari Marcondes 37310012844
07/01/2025,-246.00,677d977e-4abc-4d8a-be3b-96e75f85f394,Transferência enviada pelo Pix - Tiago Santos Toledo
07/01/2025,70.00,677daa62-d92e-4042-8aab-87d91ec95528,Transferência recebida pelo Pix - FORCEPARTS COMERCIO DE PECAS E IMPLEMENT
07/01/2025,-22.00,677dd55e-1490-4232-b0ec-2a34d0d8b38c,Compra no débito - Alessandro
07/01/2025,60.00,677dd874-f2ac-4538-ab9a-e4238029aff1,Transferência Recebida - Gabriel Henrique Paiva da Silva
08/01/2025,-23.00,677e11a1-f7b3-4e3b-9b42-0aa6b32c30fd,Compra no débito - Churrascaria Angus Gri
08/01/2025,-200.00,677e185c-7810-49d9-9cce-d1e5c7540243,Compra no débito - Autopostobrutus
08/01/2025,-10.90,677e1dd3-2b54-4d5a-a8e7-793a8ca3516a,Compra no débito - Entrevias Concessionar
08/01/2025,-8.50,677e23e0-01b0-484c-a255-cfef8d4334e9,Compra no débito - Entrevias Concessionar
08/01/2025,48.00,677e4ea7-e3f8-4af6-8903-1f4b4b6fbeaa,Transferência recebida pelo Pix - WILLIAM EDUARDO BRANCO BUSSOM
08/01/2025,185.00,677e5eeb-cdbb-4767-9c56-93aa88c7b936,Transferência recebida pelo Pix - MARCO ANTONIO MAXIMO E. P. P. ME
08/01/2025,70.00,677e6945-eb4e-4957-ba20-8fbd98488434,Transferência recebida pelo Pix - RICARDO ALEXANDRE BIZELI
08/01/2025,-180.00,677e79a2-26be-43f9-84ca-a10fced3a717,Transferência enviada pelo Pix - Lindomar Ferreira da Silva
08/01/2025,-60.00,677e9ced-cc98-4575-869b-f3ed123c5ebe,Transferência enviada pelo Pix - Marcio Candido Rosa
08/01/2025,-24.00,677ea20a-5b1a-4d71-8083-10c25944352a,Compra no débito - Rib Minas Alimentao
08/01/2025,50.00,677ebd2c-ce24-45d9-bb0a-22a8167e6273,Transferência recebida pelo Pix - MAXLUB COMERCIO DE PECAS PARA COMPRESSORES LTDA
08/01/2025,-170.00,677ebe3b-f32e-4ad7-a3e7-73ea76ded5bc,Transferência enviada pelo Pix - João Vitor Parise
08/01/2025,50.00,677ed5cb-2e47-459f-a9cc-b2e3ee3da89e,Transferência recebida pelo Pix - CAIO CESAR VILELA 37412765884
08/01/2025,271.59,677eebee-1471-4f9d-b331-9c7dac0f2b23,Transferência recebida pelo Pix - CLEOMAR MARCOS
08/01/2025,-15.97,677eef43-272a-4d6b-bdd6-e45559f0d143,Compra no débito - Galpaodacerveja
08/01/2025,1570.00,677f1173-5e5c-48e9-a463-4e1269e8079f,Transferência recebida pelo Pix - AVILA TRANSPORTES
08/01/2025,-1570.00,677f1194-2908-452d-a477-a490f080b83c,Transferência enviada pelo Pix - Alex Sandro Maziero
08/01/2025,-39.90,677f27ab-7318-48cb-b6a2-36a2c14ecd41,Compra no débito - Bello Gusto Ribeirao
09/01/2025,-17.66,677f7fe1-acc8-4f9a-adac-7c54eebf462b,Transferência enviada pelo Pix - RAIA DROGASIL SA
09/01/2025,-249.87,677fa07c-0340-4d9a-93ea-a52ad72ca93d,Transferência enviada pelo Pix - Marcio Candido Rosa
09/01/2025,789.00,677fa121-6f38-480e-b629-206b868cb595,Transferência recebida pelo Pix - AVILA TRANSPORTES
09/01/2025,-250.00,677fa13c-2589-4f79-90e3-fd9cc443ef9d,Transferência enviada pelo Pix - MARCIO CANDIDO ROSA
09/01/2025,-539.00,677fad5b-c7b7-4613-80a8-715f19a6db71,Transferência enviada pelo Pix - Victor Henrique de Jesus Lisboa
09/01/2025,60.00,677fbe6e-4ea9-4c04-832e-6ac6fce3dee5,Transferência recebida pelo Pix - FERREIRA STELUTI IND DE PLAST
09/01/2025,70.00,677fd020-8d34-40db-8430-3bd2c9027f76,Transferência Recebida - Luiz Henrique Santos Garcia
09/01/2025,-30.00,677fdfeb-6cae-490a-8a6b-bff7844e506c,Transferência enviada pelo Pix - João Vitor Parise
09/01/2025,-35.50,677ffaf3-3dfc-425d-8cc2-fa3ba428c98e,Compra no débito - Gm4autopostoltda
09/01/2025,60.00,677ffd44-aa88-4bea-93ca-6242e3cc7a14,Transferência recebida pelo Pix - LZP COMERCIAL LTDA
09/01/2025,110.00,67800554-4780-4940-af20-8480617e6d4f,Transferência Recebida - Luiz Henrique Santos Garcia
09/01/2025,60.00,67800fed-e450-4700-91a9-7b3e90206c8e,Transferência Recebida - Diego Amor Quinteiro
09/01/2025,-13.40,678020b7-f7df-40e7-b6ed-53636b71104f,Compra no débito - Entrevias Concessionar
09/01/2025,60.00,67802f32-7fe4-4149-8565-40ff4ca146f4,Transferência recebida pelo Pix - FIBERVASOS INDUSTRIA E COMERCIO LTDA
09/01/2025,-13.40,6780380c-95e3-4bb9-8d72-00bdb66d184e,Compra no débito - Entrevias Concessionar
09/01/2025,-320.00,678039eb-4259-47ed-9d8c-646f21f97a83,Compra no débito - Dp Sales Oliveira
09/01/2025,40.00,678075f1-40c6-46b1-bb34-82a05ef01962,Transferência Recebida - ALAN BELUZI 38875959803
09/01/2025,53.00,6780778f-124c-4389-86e4-ac24810fafc7,Transferência recebida pelo Pix - GUILHERME BIANCHI MORENO
09/01/2025,-52.00,678079bf-2e28-4a9f-a697-a2c30a3cb94d,Transferência enviada pelo Pix - LILIAN CRISTINA AMBROSIO DE OLIVEIRA
09/01/2025,-40.00,678079d7-9da5-4dcb-91d3-9664b782b3be,Transferência enviada pelo Pix - ALAN BELUZI 38875959803
10/01/2025,254.45,6780f407-44e3-4806-b25f-ee9776e70bf5,Transferência recebida pelo Pix - FORCEPARTS COMERCIO DE PECAS E IMPLEMENT
10/01/2025,60.00,6780f6ec-a607-4237-a103-53d38f2e06c7,Transferência Recebida - Marlom Messias dos Santos
10/01/2025,-24.49,6781132d-7dc5-434b-accf-5af8615da9f1,Compra no débito - Auto Posto Via Brasil
10/01/2025,-180.00,67811cd0-8b66-4ba8-985c-5ade75263eb5,Transferência enviada pelo Pix - Victor Henrique de Jesus Lisboa`
};

// Função para carregar dados de exemplo
function carregarDadosExemplo() {
    try {
        const transacoes = extratosManager.carregarExtratos(dadosExemplo.inter, dadosExemplo.nubank);
        transacoesFiltradas = transacoes;
        
        mostrarResultados();
        populateFilters();
        
        // Atualizar interface para mostrar que dados de exemplo foram carregados
        const uploadSection = document.querySelector('.upload-section');
        uploadSection.innerHTML = `
            <h2>📁 Dados de Exemplo Carregados</h2>
            <p style="text-align: center; color: #4a5568; margin-bottom: 20px;">
                Dados de exemplo dos extratos do Banco Inter e Nubank foram carregados para demonstração.
            </p>
            <div style="text-align: center;">
                <button class="btn" onclick="location.reload()">🔄 Carregar Novos Arquivos</button>
            </div>
        `;
        
    } catch (error) {
        console.error('Erro ao carregar dados de exemplo:', error);
    }
}