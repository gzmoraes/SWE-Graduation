#Função para cadastrar um novo produto.
def cadastro(): 
    cardapio = open("cardapio.txt", "a+")
    item = input("\nDigite o Nome do Item:\n")
    valor = float(input("Digite o Valor do item:\n"))
    cod = int(input("Digite o código do item:\n"))

    cardapio.write(F"\n{cod} - ")
    cardapio.write(F"{item} - ")
    cardapio.write(F"R${valor}")
    cardapio.close()

#Fução para alterar um produto
def alterarProduto():
    codigo = input("\nDigite o código do item que deseja alterar:\n")
    novoItem = input("Digite o novo nome do item:\n")
    novoValor = input("Digite o novo valor do item:\n")

    cardapio = open("cardapio.txt", "r")
    linhas = cardapio.readlines()
    cardapio.close()

    cardapio = open("cardapio.txt", "w")
    for linha in linhas:
        if str(codigo) in linha:
            cardapio.write(f"{codigo} - {novoItem} - R${novoValor}\n")
        else:
            cardapio.write(linha)
    cardapio.close()
    print("\nProduto alterado com sucesso.")

#Função para apagar produto especifico com base no cod dele.
def apagarProduto():
    codigo = input("\nDigite o código do item que deseja apagar:\n")

    cardapio = open("cardapio.txt", "r")
    linhas = cardapio.readlines()
    cardapio.close()

    cardapio = open("cardapio.txt", "w")
    for linha in linhas:
        if str(codigo) not in linha:
            cardapio.write(linha)
    cardapio.close()
    print("\nProduto apagado com sucesso.")

#Exibe o Cardapio
def chamarCardapio():
    cardapio = open("cardapio.txt", "r")
    print(cardapio.read())
    cardapio.close()

#Cria o pedido e armazena os itens selecionados
def procurarItem(codProcurado):
    encontrado = False
    procurar = open("cardapio.txt", "r")
    for procurado in procurar:
        if procurado.startswith(f"{codProcurado} "):
            quantidade = int(input("Digite a quantidade desejada:\n"))
            partes = procurado.strip().split(" - ")
            if len(partes) == 3:
                nome = partes[1]
                valor_str = partes[2].replace("R$", "").strip()
                if valor_str.endswith("."):
                    valor_str = valor_str[:-1]
                valor_unitario = float(valor_str)
                total_item = valor_unitario * quantidade
                pedidotxt = open("Pedido.txt", "a+")
                pedidotxt.write(f"{quantidade}x {nome} - R${total_item:.2f}\n")
                pedidotxt.close()
                print(f"{quantidade}x {nome} - R${total_item:.2f}")
                encontrado = True
            break
    if not encontrado:
        print("Código não encontrado.")

#Fializa o pedido e mostra a soma total
def finalizarPedido():
    pedidotxt = open("Pedido.txt", "r")
    linhas = pedidotxt.readlines()
    pedidotxt.close()

    total = 0.0

    print("\n--- PEDIDO ATUAL ---\n")
    for linha in linhas:
        print(linha.strip())
        if "R$" in linha:
            partes = linha.split("R$")
            if len(partes) > 1:
                valor_txt = partes[1].strip()
                if valor_txt.endswith("."):
                    valor_txt = valor_txt[:-1]
                valor = float(valor_txt)
                total += valor

    print(f"\nTotal do pedido: R$ {total:.2f}")

    #Pergunta se quer finalizar o pedido
    confirmar = input("\nDeseja confirmar o pedido? (s/n):\n").lower()

    if confirmar == "s":
        nome_cliente = input("Digite o nome do cliente:\n")

        #Adiciona o pedido em um txt de historico
        historico = open("Historico.txt", "a+")
        historico.write(f"\nCliente: {nome_cliente}\n")
        for linha in linhas:
            historico.write(linha)
        historico.write(f"Total: R${total:.2f}\n")
        historico.write("----------------------------\n")

        historico.close()
        print("Pedido confirmado e salvo no histórico. Obrigado!")
        open("Pedido.txt", "w").close()
    else:
        print("Pedido cancelado.")
        open("Pedido.txt", "w").close()

#Função para chamar o menu inicial
def menu():
    print("1 - Administrador\n" \
    "2 - Operador\n" \
    "0 - Sair\n")

#Função para chamar o menu de administrador 
def menuAdm():
    print("\n1 - Cadastrar Produto\n" \
        "2 - Listar Protudos\n" \
        "3 - Alterar Produto\n" \
        "4 - Apagar Produto\n" \
        "0 - Voltar\n")

#Começa o programa
start = True
while (start == True):
    menu()

    opcoes = int(input("Escolha uma Opção:\n"))

    adm = False
    operador = False

    if(opcoes == 1):
        adm = True
    elif(opcoes == 2):
        operador = True
        open("Pedido.txt", "w").close()  # limpa pedido antigo
    else:
        start = False
    
    # aba de administrador 
    while(adm == True):
        menuAdm()

        opcoesAdm = int(input("Escolha uma opção:\n"))

        if(opcoesAdm == 1):
            chamarCardapio()
            cadastro()
        elif(opcoesAdm == 2):
            chamarCardapio()
        elif(opcoesAdm == 3):
            chamarCardapio()
            alterarProduto()
        elif(opcoesAdm == 4):
            chamarCardapio()
            apagarProduto()
        else:
            adm = False

    # aba de operação
    while(operador == True):
        print("\nCardapio:")
        chamarCardapio()
        pedido = int(input("\nDigite o Código desejado:\n"))
        procurarItem(pedido)

        sair = int(input("1 - Finalizar Pedido | 2 - Continuar\n"))

        if(sair == 1):
            finalizarPedido()
            operador = False
        elif(sair != 2):
            print("Número inválido")