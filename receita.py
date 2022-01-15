"""Neste módulo encontra-se a classe necessária para cadastrar uma receita.

No arquivo encontra-se a implementação de uma classe: Receita

Autor: Gustavo Guerreiro
"""
import sqlite3
import conta

class Receita:
    """A classe receita representa uma receita, possuindo características e 
    métodos
    """
    def __init__(self, valor: float, data_recebimento: str, 
    data_recebimento_esperado: str, descricao: str, conta: int, 
    tipo_receita: str):
        """Cria uma instância do classe Receita.

        Args:
            valor (float): Valor da receita.
            data_recebimento (str): Data em que o dinheiro foi recebido.
            data_recebimento_esperado (str): Data em que se esperava receber o
            dinheiro.
            descricao (str): Descrição da receita.
            conta (int): Número de identificação da conta que recebeu o 
            dinheiro da receita.
            tipo_receita (str): Tipo da receita (Ex: Salário, presente, prêmio).
        """
        self.valor = valor
        self.data_recebimento = data_recebimento
        self.data_recebimento_esperado = data_recebimento_esperado
        self.descricao = descricao
        self.conta = conta
        self.tipo_receita = tipo_receita

    def criar_tabela_receita():
        """Cria uma tabela que representa as receitas.
        """
        conexao = sqlite3.connect("controleFinancas.bd")
        conexao.execute("PRAGMA foreign_keys = 1")
        cursor = conexao.cursor()
        cursor.execute("""
        create table if not exists receita
        (idReceita integer primary key,
        valor real not null,
        dataRecebimento date,
        dataRecebimentoEsperado date,
        descricao text,
        conta integer not null,
        tipoReceita text,
        foreign key (conta) references conta (idConta))
        """)
        conexao.commit()
        conexao.close()

    def salvar_receita(self):
        """Insere os dados na tabela receita e adiciona o valor na conta 
        correspondente.
        """
        receita = (self.valor, self.data_recebimento, 
        self.data_recebimento_esperado, self.descricao, self.conta, 
        self.tipo_receita)
        conexao = sqlite3.connect("controleFinancas.bd")
        conexao.execute("PRAGMA foreign_keys = 1")
        cursor = conexao.cursor()
        print(receita)
        cursor.execute("""insert into receita values (null, ?, ?, ?, ?, ?, ?)
        """, receita)
        cursor.execute("select saldo + ? from conta where idConta = ?", 
        (self.valor, self.conta))
        novo_saldo = cursor.fetchone()[0]
        conexao.commit()
        conexao.close()
        conta.Conta.editar_conta(self.conta, 1, novo_saldo)

    def editar_receita(id_receita: int, opcao: int, valor):
        """Substitui um valor registrado em uma celula da tabela receita.

        Args:
            id_receita (int): Número de identificação da receita.
            opcao (int): Opção escolhida pelo usuário que representa a coluna.
            valor: Novo valor a ser inserido na célula.
        """
        opcoes = {1:"dataRecebimento", 2:"dataRecebimentoEsperado",
        3:"descricao", 4:"tipoReceita"}
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        receita = cursor.execute("select * from receita where idReceita = ?", 
        (id_receita, )).fetchone()
        if receita is None:
            print("Receita inexistente!")
        else:
            cursor.execute(f'update receita set {opcoes[opcao]} = ? where \
            idReceita = ?', (valor, id_receita))
        conexao.commit()
        conexao.close()

    def remover_receitas(id_receita: int):
        """Remove uma linha representando uma receita na tabela.

        Args:
            id_receita (int): Número de identificação da receita.
        """
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        receita = cursor.execute("select * from receita where idReceita = ?", 
        (id_receita, )).fetchone()
        if receita is None:
            print("Receita inexistente!")
        else:
            cursor.execute("delete from receita where idReceita = ?",
            (id_receita, ))
        conexao.commit()
        conexao.close()

    def listar_receitas_filtro(filtro: int, **valor):
        """Lista receitas a partir de um filtro (data ou tipo).

        Args:
            filtro (int): Valor que representa se o filtro será por data ou 
            tipo.
        """
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        match filtro:
            case 1:
                cursor.execute("select * from receita where dataRecebimento \
                between ? and ?", (valor['data_inicial'], valor['data_final'])) 
                receitas = cursor.fetchall()
                print(receitas)
            case 2:
                cursor.execute("select * from receita where tipoReceita = ?", 
                (valor['tipo_receita'], ))
                print(cursor.fetchall())
        conexao.commit()
        conexao.close()

    def listar_receitas_total():
        """Lista todos os valores da tabela receita.
        """
        conexao = sqlite3.connect("controleFinancas.bd")
        cursor = conexao.cursor()
        cursor.execute("select * from receita")
        receitas = cursor.fetchall()
        conexao.commit()
        conexao.close()
        for receita in receitas:
            print(receita)

if __name__ == "__main__":
    opcao = None
    while opcao != "0":
        opcao = input("Digite o número correspondente à função: ")
        match opcao:
            case "1":
                Receita.criar_tabela_receita()
                receita1 = Receita(20, '2022-01-05', '2022-01-05', 'descrição',
                1, 'tipo')
                receita2 = Receita(20, '2022-01-10', '2022-01-07', 'descrição2',
                2, 'tipo2')
                receita3 = Receita(20, '2022-01-10', '2022-01-07', 'descrição3',
                2, 'tipo3')
                receita1.salvar_receita()
                receita2.salvar_receita()
                receita3.salvar_receita()
            case "2":
                Receita.editar_receita(1,1,'2021-01-04')
            case "3":
                Receita.remover_receitas(3)
            case "4":
                selecao = input("Digite '1' para seleção por data e '2' para"
                + "seleção por tipo.")
                match selecao:
                    case "1":
                        Receita.listar_receitas_filtro(1, data_inicial = '2022-01-07', data_final = '2022-01-12')
                    case "2":
                        Receita.listar_receitas_filtro(2, tipo_receita = "tipo")
            case "5":
                Receita.listar_receitas_total()