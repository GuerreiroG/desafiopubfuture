"""Neste módulo encontra-se a classe necessária para cadastrar uma receita.

No arquivo encontra-se a implementação de uma classe: Receita

Autor: Gustavo Guerreiro
"""
import sqlite3

class Receita:

    def __init__(self, valor: float, data_recebimento: str, 
    data_recebimento_esperado: str, descricao: str, conta: int, 
    tipo_receita: str):
        self.valor = valor
        self.data_recebimento = data_recebimento
        self.data_recebimento_esperado = data_recebimento_esperado
        self.descricao = descricao
        self.conta = conta
        self.tipo_receira = tipo_receita

    def criar_tabela_receita():
        conexao = sqlite3.connect("controleFinancas.bd")
        conexao.execute("PRAGMA foreign_keys = 1")
        cursor = conexao.cursor()
        cursor.execute("""
        create table if not exists receita
        (id_receita integer primary key,
        valor real not null,
        dataRecebimento date,
        dataRecebimentoEsperado date,
        descricao text,
        conta integer not null,
        tipoReceita text,
        foreign key (conta) references conta (id_conta))
        """)
        conexao.commit()
        conexao.close()

    def salvar_receita(self):
        receita = (self.valor, self.data_recebimento, 
        self.data_recebimento_esperado, self.descricao, self.conta, 
        self.tipo_receira)
        conexao = sqlite3.connect("controleFinancas.bd")
        conexao.execute("PRAGMA foreign_keys = 1")
        cursor = conexao.cursor()
        cursor.execute("""insert into receita values (null, ?, ?, ?, ?, ?, ?)
        """, receita)
        conexao.commit()
        conexao.close()

    def editar_receita(id_receita, opcao, valor):
        opcoes = {1:"valor", 2:"dataRecebimento", 3:"dataRecebimentoEsperado",
        4:"descricao", 5:"conta", 6:"tipoReceita"}
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        receita = cursor.execute("select * from conta where idReceita = ?", 
        (id_receita, )).fetchone()
        if receita is None:
            print("Receita inexistente!")
        else:
            cursor.execute(f'update receita set {opcoes[opcao]} = ? where \
            idReceita = ?', (valor, id_receita))
        conexao.commit()
        conexao.close()

    def remover_receitas(id_receita):
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        receita = cursor.execute("select * from conta where idReceita = ?", 
        (id_receita, )).fetchone()
        if receita is None:
            print("Conta inexistente!")
        else:
            cursor.execute("delete from conta where idReceita = ?",
            (id_receita, ))
        conexao.commit()
        conexao.close()

    def listar_receitas_filtro(filtro, **valor):
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        match filtro:
            case "1":
                cursor.execute("select * from receita where dataRecebimento \
                between ? and ?", (valor['data_inicial'], valor['data_final'])) 
                receitas = cursor.fetchall()
                print(receitas)
            case "2":
                cursor.execute("select * from receita where tipoReceita = ?", 
                (valor['tipo_receita']))

        conexao.commit()
        conexao.close()

    def listar_receitas_total():
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        cursor.execute("select * from receita")
        receitas = cursor.fetchall()
        conexao.commit()
        conexao.close()
        for receita in receitas:
            print(receita)