# Menu principal de acesso
def menu():
    print("\n1 - Administrador\n" \
          "2 - Operador\n" \
          "0 - Sair\n")

# Menu para opções do administrador
def menuAdm():
    print("\n1 - Cadastrar Produto\n" \
          "2 - Listar Protudos\n" \
          "3 - Alterar Produto\n" \
          "4 - Apagar Produto\n" \
          "0 - Voltar\n")

# Cadastra novos itens no cardápio
def cadastro():
    arquivo = open('cardapio.txt','r')
    linhas = arquivo.readlines()
    arquivo.close()

    listaGeral = []
    listaId = []


    desc = input('Insira o Nome do Item:\n')
    while desc == "":
        desc = input('Nome invalido! Insira o Nome do Item:\n')
    valor = input('Insira o valor do Produto:\n')
    while valor == "" or not valor.isdigit():
        valor = input('Valor Invalido! Insira o valor do Produto:\n')


    for i in linhas:
        colunas = i.strip().split(';') 
        idCol = int(colunas[0])
        descCol = colunas[1]
        valorCol = float(colunas[2])
        
        listaId.append(idCol)
        linha = f'{idCol};{descCol};{valorCol}\n'
        listaGeral.append(linha)

    if len(listaId) == 0:
        id = 100
    else:
        id = max(listaId) + 1

    novaLinha = f'{id};{desc};{valor}\n'
    listaGeral.append(novaLinha)
    listaGeral.sort()

    arquivo = open('cardapio.txt','w')
    arquivo.writelines(listaGeral)
    arquivo.close()

# Listar o cardapio
def listar():
    arquivo = open('cardapio.txt','r')
    linhas = arquivo.readlines()
    arquivo.close()

    for i in linhas:
        colunas = i.strip().split(';')
        idCol = int(colunas[0])
        descCol = colunas[1]
        valorCol = float(colunas[2])

        print(f'ID: {idCol} | {descCol} | R${valorCol}')

#Função para editar um produto com base no ID dele
def editar():
    arquivo = open('cardapio.txt','r')
    linhas = arquivo.readlines()
    arquivo.close()

    listaGeral = []

    id = int(input('Digite o Id do código item que deseja editar:\n'))

    for i in linhas:
        colunas = i.strip().split(';')
        idCol = int(colunas[0])
        descCol = colunas[1]
        valorCol = float(colunas[2])

        if id == idCol:
            novoNome = input('Digite o Novo Nome:\n')
            while novoNome == "":
                novoNome = input('Nome invalido! Insira o Nome do Item:\n')

            novoValor = input('Insira o valor do Produto:\n')
            while novoValor == "" or not novoValor.isdigit():
                novoValor = input('Valor Invalido! Insira o valor do Produto:\n')

            novaLinha = f'{id};{novoNome};{novoValor}\n'
            listaGeral.append(novaLinha)
        else:
            linha = f'{idCol};{descCol};{valorCol}\n'
            listaGeral.append(linha)

    listaGeral.sort()
    arquivo = open('cardapio.txt','w')
    arquivo.writelines(listaGeral)
    arquivo.close()
    print('Produto alterado com Sucesso!')

#Função para excluir um produto
def excluir():
    arquivo = open('cardapio.txt','r')
    linhas = arquivo.readlines()
    arquivo.close()

    ids = []

    for i in linhas:
        colunas = i.strip().split(';')
        idExistentes = int(colunas[0])
        ids.append(idExistentes)

    id = int(input('Digite o ID do Produto que deseja excluir:\n'))
    validar = True
    while validar == True:
        
        if id in ids:
            validar = False
        else:
            id = int(input('ID invalido! Digite o ID do Produto que deseja excluir:\n'))
    
    listaGeral = []

    for i in linhas:
        colunas = i.strip().split(';')
        idCol = int(colunas[0])
        descCol = colunas[1]
        valorCol = float(colunas[2])

        if id == idCol:
            print('Produto Excluido com Sucesso!')
        else:
            linha = f'{idCol};{descCol};{valorCol}\n'
            listaGeral.append(linha)
    
    listaGeral.sort()
    arquivo = open('cardapio.txt','w')
    arquivo.writelines(listaGeral)
    arquivo.close()
            
# Função que permite um cliente fazer pedidos
def pedido():
    cardapio = open("cardapio.txt", "r")
    linhas = cardapio.readlines()
    cardapio.close()

    listaCod = []
    listaItem = []
    listaValor = []

    for linha in linhas:
        coluna = linha.strip().split(";")
        cod = coluna[0]
        item = coluna[1]
        valor = float(coluna[2])

        listaCod.append(cod)
        listaItem.append(item)
        listaValor.append(valor)

    nome = input("\nDigite seu nome:\n")
    while nome == "":
        print('Nome Invalido! Digite o nome:\n')
        nome = input("\nDigite seu nome:\n")

    listaPedido = []
    totalGeral = 0

    codigo = input("Digite o código do pedido desejado:\n")
    while codigo not in listaCod:
        codigo = input("Codigo Invalido! Digite o código do pedido desejado:\n")

    comecarP = True
    while comecarP == True:
        posicao = listaCod.index(codigo)

        qnt = int(input("Informe a quantidade:\n"))

        desc = listaItem[posicao]
        valorU = listaValor[posicao]
        valorF = qnt * valorU
        totalGeral += valorF

        listaPedido.append((desc, qnt, valorU, valorF))

        print(f"Adicionado: {desc} x{qnt} - Total: R${valorF:.2f}")

        sair = input("\nDeseja adicionar outro item? (s/n): ")
        if sair != "s":
            comecarP = False
        else:
            codigo = input("Digite o código do pedido desejado:\n")
            while codigo not in listaCod:
                codigo = input("Codigo Invalido! Digite o código do pedido desejado:\n")

    # Exibe o resumo final do pedido
    print("\n--- Pedido Final ---")
    for item in listaPedido:
        print(f"{item[0]} x{item[1]} - R${item[3]:.2f}")
    print(f"Total a pagar: R${totalGeral:.2f}")

    # Registra no histórico
    historico = open("historico.txt", "a+")
    historico.write(f"\nCliente: {nome}\n")
    for item in listaPedido:
        historico.write(f"Pedido: {item[0]} - Quantidade: {item[1]} - Valor Unitário: R${item[2]:.2f} - Total: R${item[3]:.2f}\n")
    historico.write(f"Valor Total do Pedido: R${totalGeral:.2f}\n")
    historico.write("-" * 40 + "\n")
    historico.close()

# Início do programa
start = True
while start:
    menu()
    opcoes = int(input("Escolha uma Opção:\n"))

    adm = False
    operador = False

    if opcoes == 1:
        user = input("Digite o usuario:\n")
        senha = input("Digite a senha:\n")
        autenticacao = 1
        while autenticacao == 1:
            if user == "adm" and senha =="123":
                adm = True
                autenticacao = 0
            else:
                print("Usuario ou senha incorretos!")
                exit = input("Voltar?(S ou N)")
                if exit.lower() == "n":
                    user = input("Digite o usuario:")
                    senha = input("Digite a senha:")
                else:
                    autenticacao = 0
    elif opcoes == 2:
        operador = True
    else:
        start = False

    # Loop do administrador
    while adm:
        menuAdm()
        opcoesAdm = int(input("Escolha uma opção:\n"))

        if opcoesAdm == 1:
            listar()
            cadastro()
        elif opcoesAdm == 2:
            listar()
        elif opcoesAdm == 3:
            listar()
            editar()
        elif opcoesAdm == 4:
            listar()
            excluir()
        else:
            adm = False

    # Loop do operador
    while operador:
        print("\nCardapio:")
        listar()
        pedido()
        operador = False
