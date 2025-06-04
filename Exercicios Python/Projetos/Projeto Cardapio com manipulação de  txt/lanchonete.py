# Função que exibe o conteúdo do cardápio
def chamarCardapio():
    print("\n---Cardapio---")
    cardapio = open("cardapio.txt", "r")
    print(cardapio.read())
    cardapio.close()

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
    # Lê o conteúdo atual do cardápio
    cardapio = open("cardapio.txt", "r")
    linhas = cardapio.readlines()
    cardapio.close()

    # Converte as linhas em tuplas (código, nome, valor)
    listaProd = []
    for linha in linhas:
        coluna = linha.strip().split(" - ")
        cod = int(coluna[0])
        nome = coluna[1]  
        valor = float(coluna[2].replace("R$", ""))
        listaProd.append((cod, nome, valor))

    # Coleta dados do novo item
    item = input("\nDigite o Nome do Item:\n")
    while(item == ""):
        print("Insira um nome válido!")
        item = input("\nDigite o Nome do Item:\n")

    valor = float(input(f"Digite o Valor do item {item}:\n"))
    cod = int(input("Digite o código do item:\n"))

    # Adiciona o novo produto
    listaProd.append((cod, item, valor))
    listaProd.sort()  # Ordena por código

    # Sobrescreve o arquivo com o novo item incluso
    cardapio = open("cardapio.txt", "w")
    for produto in listaProd:
        cardapio.write(f"{produto[0]} - {produto[1]} - R${produto[2]:.2f}\n")
    cardapio.close()

    print("\nItem cadastrado com sucesso!")

# Altera um item existente no cardápio
def editar():
    cardapio = open("cardapio.txt","r")
    linhas = cardapio.readlines()
    cardapio.close()

    listaProd = []
    for linha in linhas:
        coluna = linha.strip().split(" - ")
        cod = int(coluna[0])
        item = coluna[1]
        valor = float(coluna[2].replace("R$",""))
        listaProd.append((cod,item,valor))

    edit = int(input("\nDigite o codigo do item que deseja editar:\n"))

    for i in range(len(listaProd)):
        if(listaProd[i][0] == edit): 
            print(f"Produto atual: {listaProd[i][1]} - R${listaProd[i][2]:.2f}")
            novoNome = input("\nDigite o novo nome\n")
            novoValor = float(input("Digite o novo valor\n"))
            listaProd[i] = (edit, novoNome, novoValor)

            cardapio = open("cardapio.txt", "w")
            for produto in listaProd:
                cardapio.write(f"{produto[0]} - {produto[1]} - R${produto[2]:.2f}\n")
            cardapio.close()
            print("\nProduto alterado com sucesso!")

# Função para remover um item do cardápio
def excluir():
    cardapio = open("cardapio.txt", "r")
    linhas = cardapio.readlines()
    cardapio.close()

    listaProd = [i.strip() for i in linhas]

    cod = input("\nDigite o código do produto que deseja remover: \n")

    for linha in listaProd:
        coluna = linha.split(" - ")  
        if coluna[0] == cod:
            listaProd.remove(linha)
            print("\nProduto removido com sucesso!")
            break
    else:
        print("\nProduto com esse código não foi encontrado.")

    cardapio = open("cardapio.txt", "w")
    for item in listaProd:
        cardapio.write(item + "\n")
    cardapio.close()

    print("\nLista atualizada:")
    for item in listaProd:
        print(item)

# Função que permite um cliente fazer pedidos
def pedido():
    cardapio = open("cardapio.txt", "r")
    linhas = cardapio.readlines()
    cardapio.close()

    listaCod = []
    listaItem = []
    listaValor = []

    for linha in linhas:
        coluna = linha.strip().split(" - ")
        cod = int(coluna[0])
        item = coluna[1]
        valor = float(coluna[2].replace("R$", ""))

        listaCod.append(cod)
        listaItem.append(item)
        listaValor.append(valor)

    nome = input("\nDigite seu nome:\n")
    listaPedido = []
    totalGeral = 0
    comecarP = True

    while comecarP:
        codigo = int(input("Digite o código do pedido desejado:\n"))

        if codigo in listaCod:
            posicao = listaCod.index(codigo)
            qnt = int(input("Informe a quantidade:\n"))

            desc = listaItem[posicao]
            valorU = listaValor[posicao]
            valorF = qnt * valorU
            totalGeral += valorF

            listaPedido.append((desc, qnt, valorU, valorF))

            print(f"Adicionado: {desc} x{qnt} - Total: R${valorF:.2f}")
        else:
            print("Código não encontrado!")

        sair = input("\nDeseja adicionar outro item? (s/n): ")
        if sair != "s":
            comecarP = False

    # Exibe o resumo final do pedido
    print("\n--- Pedido Final ---")
    for item in listaPedido:
        print(f"{item[0]} x{item[1]} - R${item[3]:.2f}")
    print(f"Total a pagar: R${totalGeral:.2f}")

    # Registra no histórico
    historico = open("historico.txt", "a")
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
        user = input("Digite o usuario:")
        senha = input("Digite a senha:")
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
            chamarCardapio()
            cadastro()
        elif opcoesAdm == 2:
            chamarCardapio()
        elif opcoesAdm == 3:
            chamarCardapio()
            editar()
        elif opcoesAdm == 4:
            chamarCardapio()
            excluir()
        else:
            adm = False

    # Loop do operador
    while operador:
        print("\nCardapio:")
        chamarCardapio()
        pedido()
        operador = False
