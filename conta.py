"""Neste módulo encontra-se a classe necessária para cadastrar uma conta.

No arquivo encontra-se a implementação de uma classe: Conta

Autor: Gustavo Guerreiro
"""
import sqlite3

class Conta:
    """A classe Conta representa uma conta cadastrada no sistema, possuindo
    diferentes atributos e métodos.
    """
    def __init__(self, saldo: float, tipo_conta: str, 
    instituicao_financeira: str):
        """Cria uma intância do objeto Conta

        Args:
            saldo (floar): Quantidade de dinheiro na conta.
            tipo_conta (str): Tipo da conta (Ex: carteira, conta corrente, 
            poupança).
            instituicao_financeira (str): A instituição financeira. 
        """
        self.saldo = saldo
        self.tipo_conta = tipo_conta
        self.instituicao_financeira = instituicao_financeira

    def criar_tabela_conta():
        """Cria uma tabela que representa as contas.
        """
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        cursor.execute("""
        create table if not exists conta
        (idConta integer primary key,
        saldo real not null,
        tipoConta text not null,
        instituicaoFinanceira text not null)
        """)
        conexao.commit()
        conexao.close()

    def salvar_conta(self):
        """Insere os dados da conta na tabela do Banco de Dados
        """
        conta = (self.saldo, self.tipo_conta, self.instituicao_financeira)
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        cursor.execute("""insert into conta values (null, ?, ?, ?)""", conta)
        conexao.commit()
        conexao.close()

    def editar_conta(id_conta: int, opcao: int, valor):
        """Substitui um valor registrado em uma celula da tabela conta.

        Args:
            id_conta (int): Número de identificação da conta.
            opcao (int): Opção escolhida pelo usuário que representa a coluna.
            valor: Novo valor a ser inserida na célula.
        """
        opcoes = {1:"saldo", 2:"tipoConta", 3:"instituicaoFinanceira"}
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        conta = cursor.execute("select * from conta where idConta = ?", 
        (id_conta, )).fetchone()
        if conta is None:
            print("Conta inexistente!")
        else:
            cursor.execute(f'update conta set {opcoes[opcao]} = ? where \
            idConta = ?', (valor, id_conta))
        conexao.commit()
        conexao.close()

    def remover_conta(id_conta: int):
        """Remove uma linha representando uma conta na tabela.

        Args:
            id_conta (int): Número de identificação da conta.
        """
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        conta = cursor.execute("select * from conta where idConta = ?", 
        (id_conta, )).fetchone()
        if conta is None:
            print("Conta inexistente!")
        else:
            cursor.execute("delete from conta where idConta = ?",
            (id_conta, ))
        conexao.commit()
        conexao.close()

    def listar_contas():
        """Lista todos os valores da tabela conta.
        """
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        for linha in cursor.execute("select * from conta"):
            print(linha)
        conexao.commit()
        conexao.close()
    
    def tranferir_saldo(id_conta1: int, valor: float, id_conta2: int):
        """Desconta certo valor do saldo de uma conta e acrescenta em outra.

        Args:
            id_conta1 (int): Número de identificação da conta que irá ter o valor 
            descontado.
            valor (float): valor a ser transferido.
            id_conta2 (int): Número de identificação da conta que irá ter o valor
            acrescentado.
        """
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        cursor.execute("select saldo - ? from conta where \
        idConta = ?", (valor, id_conta1))
        novo_saldo1 = cursor.fetchone()[0]
        cursor.execute("select saldo + ? from conta where \
        idConta = ?", (valor, id_conta2))
        novo_saldo2 = cursor.fetchone()[0]

        if novo_saldo1 < 0:
            print("Saldo Insuficiente")
        else:
            Conta.editar_conta(id_conta1, 1, novo_saldo1)
            Conta.editar_conta(id_conta2, 1, novo_saldo2)
        conexao.commit()
        conexao.close()

    def listar_saldo(id_conta: int):
        """Exibe o saldo de uma conta especificada.

        Args:
            id_conta (int): Número de identificação da conta.
        """
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        cursor.execute("select saldo from conta where idConta = ?", 
        (id_conta, ))
        saldo = cursor.fetchone()[0]
        conexao.commit()
        conexao.close()
        print(f"Saldo total: {saldo}.")

if __name__ == "__main__":
    opcao = None
    while opcao != "0":
        opcao = input("Digite o número correspondente à função: ")
        match opcao:
            case "1":
                Conta.criar_tabela_conta()
                conta1 = Conta(10.00, "poupança", "pessoal")
                conta2 = Conta(20.50, "conta corrente", "publica")
                conta3 = Conta(30.00, "conta corrente", "banco")
                conta1.salvar_conta()
                conta2.salvar_conta()
                conta3.salvar_conta()
            case "2":
                Conta.editar_conta(1,1,15)
            case "3":
                Conta.remover_conta(3)
            case "4":
                Conta.listar_contas()
            case "5":
                Conta.tranferir_saldo(1,5,2)
            case "6":
                Conta.listar_saldo(1)