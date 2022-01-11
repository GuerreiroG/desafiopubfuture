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
        self.saldo = saldo
        self.tipo_conta = tipo_conta
        self.instituicao_financeira = instituicao_financeira

    def cadastrar_conta(self):
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

    @staticmethod
    def editar_conta(id_conta, opcao, valor):
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

    @staticmethod
    def remover_conta(id_conta):
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

    @staticmethod
    def listar_contas():
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        for linha in cursor.execute("select * from conta"):
            print(linha)
        conexao.commit()
        conexao.close()
    
    def tranferir_saldo(self, id_conta1, valor, id_conta2):
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        novo_saldo1 = cursor.execute("select saldo + ? from conta where \
        idConta = ?", (valor, id_conta1))
        self.editar_conta(id_conta1, 1, novo_saldo1)
        novo_saldo2 = cursor.execute("select saldo - ? from conta where \
        idConta = ?", (valor, id_conta2))
        self.editar_conta(id_conta2, 1, novo_saldo2)
        conexao.commit()
        conexao.close()

    def listar_saldo(id_conta):
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        saldo = cursor.execute("select saldo from conta where idConta = ?", 
        (id_conta, ))
        conexao.commit()
        conexao.close()
