#Exibe o Cardapio
def chamarCardapio():
    cardapio = open("cardapio.txt", "r")
    print(cardapio.read())
    cardapio.close()

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
  
#Função para cadastrar um novo produto.
def cadastro(): 
    cardapio = open("cardapio.txt", "a+")
    item = input("\nDigite o Nome do Item:\n")
    while (item == ""):
        print("Insira um nome valido!")
        item = input("\nDigite o Nome do Item:\n")
    valor = float(input(f"Digite o Valor do item {item}:\n"))
    while (valor == "" or valor.isalpha()):
        print("Insira um valor valido!")
        valor = float(input("Digite o Valor do item:\n"))
    cod = int(input("Digite o código do item:\n"))
    while (cod == ""):
        print("Insira um codigo valido!")
        cod = int(input("Digite o código do item:\n"))

    cardapio.write(F"\n{cod} - ")
    cardapio.write(F"{item} - ")
    cardapio.write(F"R${valor}")
    cardapio.close()

def editarProtuto():
    cardapio = open("cardapio.txt", "r")
    linha = cardapio.readlines()   

    alterar = input("Insira o cod do produto que dejeja alterar:\n")
    while (alterar == ""):
        print("Código inválido")
        alterar = input("Insira o cod do produto que dejeja alterar:\n")

    encontrado = 0  

    for i in range(len(linha)):
        if (linha[i].startswith(alterar + " - ")):
            print(f"Alterando {linha[i].strip()}")
            novaDesc = input("Digite o nome do item:\n")
            novoPreco = input("Digite o valor:\n")

            linha[i] = f"{alterar} - {novaDesc} - {novoPreco}\n"

            encontrado = 1
            break

    if (encontrado == 1):
        cardapio = open("cardapio.txt", "w")
        cardapio.writelines(linha)
        cardapio.close()
        print("Produto alterado com sucesso")
        
    else:
        print("Produto não encontrado!")
        


    

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
            editarProtuto()
            
        elif(opcoesAdm == 4):
            chamarCardapio()
            
        else:
            adm = False

    # aba de operação
    while(operador == True):
        print("\nCardapio:")
        chamarCardapio()
        pedido = int(input("\nDigite o Código desejado:\n"))

        sair = int(input("1 - Finalizar Pedido | 2 - Continuar\n"))

        if(sair == 1):
        
            operador = False
        elif(sair != 2):
            print("Número inválido")