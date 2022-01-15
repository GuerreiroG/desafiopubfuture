"""Neste módulo encontra-se a classe necessária para realizar a interação
entre o usuário e o gerenciador de finanças

No arquivo encontra-se a implementação de uma classe: Interface.

Autor: Gustavo Guerreiro.
"""
import conta
import receita
import despesa

class Interface:
    """Parte do código na qual o usuário irá interagir.
    """
    def __init__(self):
        """Cria uma instância da classe interface
        """
        print("Digite '1' para cadastrar uma conta")
        print("Digite '2' para deletar uma conta")
        print("Digite '3' para atualizar uma conta")
        print("Digite '4' para listar todas as contas")
        print("Digite '5' transferir saldo entre contas")
        print("Digite '6' para cadastrar uma receita")
        print("Digite '7' para editar uma receita")
        print("Digite '8' para remover uma receita")
        print("Digite '9' para listar as receitas por data")
        print("Digite '10' para listar receitas por tipo")
        print("Digite '11' para listar todas as receitas")
        print("Digite '12' para cadastrar uma despesa")
        print("Digite '13' para editar uma despesa")
        print("Digite '14' para remover uma despesa")
        print("Digite '15' para listar as depesas por data")
        print("Digite '16' para listar despesas por tipo")
        print("Digite '17' para listar todas as despesas")
        while True:
            try:
                resp = int(input("Digite a opção escolhida: "))
                match resp:
                    case 0:
                        break
                    case 1:
                        self.cadastrar_conta()
                    case 2:
                        self.deletar_conta()
                    case 3: 
                        self.atualizar_conta()
                    case 4: 
                        conta.Conta.listar_contas()
                    case 5:
                        self.transferir_saldo()
                    case 6: 
                        self.cadastrar_receita()
                    case 7: 
                        self.atualizar_receita()
                    case 8:
                        self.deletar_receita()
                    case 9: 
                        self.listar_receitas_por_data()
                    case 10:
                        self.listar_receitas_por_tipo()
                    case 11:
                        receita.Receita.listar_receitas_total()
                    case 12:
                        self.cadastrar_despesa()
                    case 13:
                        self.atualizar_despesa()
                    case 14:
                        self.deletar_despesa()
                    case 15:
                        self.listar_despesas_por_data()
                    case 16:
                        self.listar_despesas_por_tipo()
                    case 17:
                        despesa.Despesa.listar_despesas_total()
            except:
                print("Erro!")

    
    def cadastrar_conta(self):
        """Insere os dados na tabela conta.
        """
        saldo = float(input("Digite o saldo da conta: "))
        tipo_conta = input("Digite o tipo da conta: ")
        instituicao_financeira = input("Digite a instituição financeira: ")
        nova_conta = conta.Conta(saldo, tipo_conta, instituicao_financeira)
        conta.Conta.criar_tabela_conta()
        nova_conta.salvar_conta()

    def deletar_conta(self):
        """Deleta uma linha representando uma conta a partir de um id fornecido.
        """
        id_conta = float(input("Digite o id da conta: "))
        conta.Conta.remover_conta(id_conta)
    
    def atualizar_conta(self):
        """Atualiza os dados da conta.
        """
        id_conta = float(input("Digite o id da conta: "))
        print("Opções de atualização:")
        print("1 - Saldo")
        print("2 - Tipo da Conta")
        print("3 - Instituição Financeira")
        opcao = int(input("Digite a opção escolhida: "))
        valor = input("Digite o novo dado: ")
        conta.Conta.editar_conta(id_conta, opcao, valor)

    def transferir_saldo(self):
        """Tranfere valores de uma conta para outra.
        """
        pagador = int(input("Digite o id da conta que irá pagar: "))
        valor = float(input("Digite o valor da transferência: "))
        recebedor = int(input("Digite o id da conta que irá receber o pagamento: "))
        conta.Conta.tranferir_saldo(pagador, valor, recebedor)

    def cadastrar_receita(self):
        """Insere os dados na tabela receita.
        """
        valor = float(input("Digite o valor: "))
        data_recebimento = input("Digite a data do recebimento (formato AAAA-MM-DD): ")
        data_recebimento_esperado = input("Digite a data esperada do recebimento (formato AAAA-MM-DD): ")
        descricao = input("Digite a descrição da receita: ")
        conta = int(input("Digite o id da conta: "))
        tipo_receita = input("Digite o tipo da receita: ")
        nova_receita = receita.Receita(valor, data_recebimento, data_recebimento_esperado, 
        descricao, conta, tipo_receita)
        receita.Receita.criar_tabela_receita()
        nova_receita.salvar_receita()

    def atualizar_receita(self):
        """Atualiza os dados da tabela receita.
        """
        print("Opções de atualização:")
        print("1 - Data de Recebimento")
        print("2 - Data esperada do Recebimento")
        print("3 - Descrição")
        print("4 - Tipo de Receita")
        opcao = int(input("Digite a opção escolhida: "))
        id_receita = int(input("Digite o id da receita a ser alterada: "))
        valor = input("Digite o novo valor: ")
        receita.Receita.editar_receita(id_receita, opcao, valor)

    def deletar_receita(self):
        """Deleta a linha representando uma receita a partir do id fornecido.
        """
        id_receita = float(input("Digite o id da receita: "))
        receita.Receita.remover_receitas(id_receita)

    def listar_receitas_por_data(self):
        """Lista as receitas a partir de duas datas fornecidas.
        """
        data_inicial = input("Digite a data de inicial: ")
        data_final = input("Digite a data final: ")
        receita.Receita.listar_receitas_filtro(1, data_inicial = data_inicial,
        data_final = data_final)

    def listar_receitas_por_tipo(self):
        """Lista as receitas a partir de um tipo fornecido.
        """
        tipo = input("Digite o tipo da receita: ")
        receita.Receita.listar_receitas_filtro(2, tipo_receita = tipo)

    def cadastrar_despesa(self):
        """Insere os dados na tabela despesa.
        """
        valor = float(input("Digite o valor: "))
        data_pagamento = input("Digite a data do pagamento (formato AAAA-MM-DD): ")
        data_pagamento_esperado = input("Digite a data esperada do pagamento (formato AAAA-MM-DD): ")
        conta = int(input("Digite o id da conta: "))
        tipo_despesa = input("Digite o tipo da despesa: ")
        nova_despesa = despesa.Despesa(valor, data_pagamento, data_pagamento_esperado, 
        conta, tipo_despesa)
        despesa.Despesa.criar_tabela_despesa()
        nova_despesa.salvar_despesa()

    def atualizar_despesa(self):
        """Atualiza os dados da tabela despesa.
        """
        print("Opções de atualização:")
        print("1 - Data de pagamento")
        print("2 - Data esperada do pagamento")
        print("3 - Tipo de despesa")
        opcao = int(input("Digite a opção escolhida: "))
        id_despesa = int(input("Digite o id da despesa a ser alterada: "))
        valor = input("Digite o novo valor: ")
        despesa.Despesa.editar_despesas(id_despesa, opcao, valor)

    def deletar_despesa(self):
        """Deleta a linha representando uma despesa a partir do id fornecido.
        """
        id_despesa = float(input("Digite o id da despesa: "))
        despesa.Despesa.remover_despesas(id_despesa)

    def listar_despesas_por_data(self):
        """Lista as despesas a partir de duas datas fornecidas.
        """
        data_inicial = input("Digite a data de inicial: ")
        data_final = input("Digite a data final: ")
        despesa.Despesa.listar_despesas_filtro(1, data_inicial = data_inicial,
        data_final = data_final)

    def listar_despesas_por_tipo(self):
        """Lista as despesas a partir de um tipo fornecido.
        """
        tipo = input("Digite o tipo da despesa: ")
        despesa.Despesa.listar_despesas_filtro(2, tipo_despesa = tipo)

if __name__ == "__main__":
    Interface()