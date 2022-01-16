# Sistema de Gerenciamento de Finanças Pessoais
Um simples sistema feito em Python 3.10.0

---
## Tabela de Conteúdos
* [Introdução](#introducao)
* [Tecnologias](#tecnologias)
* [Inicialização](#inicializacao)
* [Escopo das Funcionalidades](#escopo-das-funcionalidades)
* [Como Utilizar o Programa](#como-utilizar-o-programa)
* [Informações Extras](#informacoes-extras)

---

## Introdução
O objetivo do sistema é permitir que o usuário possa registrar as suas contas, receitas e despesas para ter um maior controle de suas finanças pessoais. Registrando o que ganha, gasta e onde guarda esse dinheiro. Trata-se de um sistema simples criado usando Python 3.10.0.

---
## Tecnologias
Para rodar o sistema são necessárias as seguintes tecnologias:
- Python 3.10.0
- SQLite3 2.6.0
 
---
## Inicialização
O programa pode ser iniciado por diversos meios que rodem códigos Python, como o Prompt de Comando ou outras ferramentas CASE como Visual Studio Code. Abaixo será feita a demonstração de como rodar o programa pelo cmd:

```
cd [Caminho do diretório em que o programa foi instalado]
python interface.py
```

Neste momento o programa deverá exibir opções para o usuário selecionar, então basta digitar o número correspondente a opção selecionado e apertar a tecla "Enter", e depois preencher com os dados que o programa pedir. Apertando "Enter" após o dado ser digitado.

---
## Escopo das funcionalidades.
O programa possui diversas funcionaliades, dentre elas pode-se citar:
- Cadastro de contas, receitas e depesas.
- Remoção, edição e listagem de contas, receitas e depesas cadastradas.
- Listagem de receitas e despesas por períodos específicos ou tipo.

---
## Como Utilizar o Programa
O programa irá exibir um texto explicitando os dados necessários para serem inseridos. Quando se insere os dados deve-se levar certos pontos em consideração:
- Em valores de número reais, principalmente números "com vírgula", as casas decimais devem ser separadas por um ponto ".", como por exemplo, se fosse cadastrar um valor de cinquenta reais e trinta e cinco centavos o usuário teria que digitar "50.35" e apertar "Enter".
- O programa irá interpretar todos os valores monetários como sendo reais, não sendo necessário especificar a moeda quando inserir o valor de algo no programa (especificar a moeda levará o programa a exibir uma mensagem de erro).
- Em diversos momentos o programa pede para que o ID de algo seja especificado, para encontrar o ID de algo cadastrado basta pedir para que o programa liste todos os elementos cadastrados daquele tipo (conta, receita ou despesa), e o primeiro valor que aparecer nas listas exibidas corresponderá ao ID.
- Quando o programa pedir um elemento que correponda a um número real, deve-se evitar o uso de texto, como espaços, letras etc. Apenas números serão suficientes, outros caracteres podem levar o programa a exibir uma mensagem de erro.
- Ao ser cadastrado uma despesa ou uma receita, o saldo na conta correspondente já é automaticamente atualizado, não sendo necessário alterá-lo manualmente.
---
## Informações Extras
Este programa foi desenvolvido por Gustavo Guerreiro para o desafio lançado pela empresa Pública chamado Pubfuture e pode ser acessado por meio do link:
https://github.com/GuerreiroG/desafiopubfuture