"""Neste módulo encontra-se a classe necessária para cadastrar uma despesa.

No arquivo encontra-se a implementação de uma classe: Despesa

Autor: Gustavo Guerreiro
"""
import sqlite3
import conta

class Despesa:

    def __init__(self, valor: float, data_pagamento: str,
    data_pagamento_esperado: str, conta: int, tipo_despesa: str):
        """Cria uma instância do classe Despesa.

        Args:
            valor (float): Valor da despesa.
            data_pagamento (str): Data em que o dinheiro foi pago.
            data_pagamento_esperado (str): Data em que se esperava pagar o
            dinheiro.
            conta (int): Número de identificação da conta que pagou o 
            dinheiro da despesa.
            tipo_despesa (str): Tipo da despesa (alimentação, educação, lazer,
            moradia, roupa, saúde, transporte etc.)
        """
        self.valor = valor
        self.data_pagamento = data_pagamento
        self.data_pagamento_esperado = data_pagamento_esperado
        self.conta = conta
        self.tipo_despesa = tipo_despesa

    def criar_tabela_despesa():
        """Cria uma tabela que representa as despesas.
        """
        conexao = sqlite3.connect("controleFinancas.bd")
        conexao.execute("PRAGMA foreign_keys = 1")
        cursor = conexao.cursor()
        cursor.execute("""
        create table if not exists despesa
        (idDespesa integer primary key,
        valor real not null,
        dataPagamento date,
        dataPagamentoEsperado date,
        conta integer not null,
        tipoDespesa text,
        foreign key (conta) references conta (idConta))
        """)
        conexao.commit()
        conexao.close()

    def salvar_despesa(self):
        """Insere os dados na tabela despesa e desconta o valor na conta 
        correspondente.
        """
        despesa = (self.valor, self.data_pagamento, 
        self.data_pagamento_esperado, self.conta, self.tipo_despesa)
        conexao = sqlite3.connect("controleFinancas.bd")
        conexao.execute("PRAGMA foreign_keys = 1")
        cursor = conexao.cursor()
        cursor.execute("select saldo - ? from conta where idConta = ?", 
        (self.valor, self.conta))
        novo_saldo = cursor.fetchone()[0]
        if novo_saldo < 0:
            print("Saldo Insuficiente!")
            conexao.commit()
            conexao.close()
        else:
            cursor.execute("""insert into despesa values (null, ?, ?, ?, ?, ?)
            """, despesa)
            conexao.commit()
            conexao.close()
            conta.Conta.editar_conta(self.conta, 1, novo_saldo)

    def editar_despesas(id_despesa: int, opcao: float, valor):
        """Substitui um valor registrado em uma celula da tabela despesa.

        Args:
            id_despesa (int): Número de identificação da despesa.
            opcao (int): Opção escolhida pelo usuário que representa a coluna.
            valor: Novo valor a ser inserido na célula.
        """
        opcoes = {1:"dataPagamento", 2:"dataPagamentoEsperado",
        3:"descricao", 4:"conta", 5:"tipoPagamento"}
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        despesa = cursor.execute("select * from despesa where idDespesa = ?", 
        (id_despesa, )).fetchone()
        if despesa is None:
            print("Despesa inexistente!")
        else:
            cursor.execute(f'update despesa set {opcoes[opcao]} = ? where \
            idDespesa = ?', (valor, id_despesa))
        conexao.commit()
        conexao.close()

    def remover_despesas(id_despesa):
        """Remove uma linha representando uma despesa na tabela.

        Args:
            id_despesa (int): Número de identificação da despesa.
        """
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        despesa = cursor.execute("select * from despesa where idDespesa = ?", 
        (id_despesa, )).fetchone()
        if despesa is None:
            print("Despesa inexistente!")
        else:
            cursor.execute("delete from despesa where idDespesa = ?",
            (id_despesa, ))
        conexao.commit()
        conexao.close()

    def listar_despesas_filtro(filtro, **valor):
        """Lista despesas a partir de um filtro (data ou tipo).

        Args:
            filtro (int): Valor que representa se o filtro será por data ou 
            tipo.
        """
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        match filtro:
            case 1:
                cursor.execute("select * from despesa where dataPagamento \
                between ? and ?", (valor['data_inicial'], valor['data_final'])) 
                despesas = cursor.fetchall()
                print(despesas)
            case 2:
                cursor.execute("select * from despesa where tipoDespesa = ?", 
                (valor['tipo_despesa'], ))
                print(cursor.fetchall())
        conexao.commit()
        conexao.close()

    def listar_despesas_total():
        """Lista todos os valores da tabela despesa.
        """
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        cursor.execute("select * from despesa")
        despesas = cursor.fetchall()
        conexao.commit()
        conexao.close()
        for despesa in despesas:
            print(despesa)

if __name__ == "__main__":
    opcao = None
    while opcao != "0":
        opcao = input("Digite o número correspondente à função: ")
        match opcao:
            case "1":
                Despesa.criar_tabela_despesa()
                despesa1 = Despesa(20, '2022-01-05', '2022-01-05', 1, 'tipo1')
                despesa2 = Despesa(20, '2020-01-05', '2020-02-05', 2, 'tipo2')
                despesa3 = Despesa(20, '2021-12-05', '2022-02-05', 3, 'tipo3')

                despesa1.salvar_despesa()
                despesa2.salvar_despesa()
                despesa3.salvar_despesa()
            case "2":
                Despesa.editar_despesas(1,1,'2021-01-04')
            case "3":
                Despesa.remover_despesas(3)
            case "4":
                selecao = input("Digite '1' para seleção por data e '2' para"
                + "seleção por tipo: ")
                match selecao:
                    case "1":
                        Despesa.listar_despesas_filtro(1, data_inicial = '2020-01-01', data_final = '2021-01-12')
                    case "2":
                        Despesa.listar_despesas_filtro(2, tipo_despesa = "tipo2")
            case "5":
                Despesa.listar_despesas_total()