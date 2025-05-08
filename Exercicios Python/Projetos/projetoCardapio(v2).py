import json
import os

# Listas relacionadas ao pedido
pedido = []
listaPedidos = []

# Listas de setup (serão preenchidas pelo arquivo JSON)
codigos = []
esp = []
preco = []

# Lista para armazenar o valor total
listaPreco = []

# Função para carregar o cardápio do arquivo .json
def carregarCardapio():
    caminho_cardapio = os.path.join(os.path.dirname(__file__), "cardapio.json")
    if os.path.exists(caminho_cardapio):
        with open(caminho_cardapio, "r") as f:
            dados = json.load(f)
            codigos.clear()
            esp.clear()
            preco.clear()
            for item in dados:
                codigos.append(item["codigo"])
                esp.append(item["nome"])
                preco.append(item["preco"])

# Função para salvar o cardápio no arquivo .json
def salvarCardapio():
    dados = [{"codigo": codigos[i], "nome": esp[i], "preco": preco[i]} for i in range(len(codigos))]
    caminho_cardapio = os.path.join(os.path.dirname(__file__), "cardapio.json")
    with open(caminho_cardapio, "w") as f:
        json.dump(dados, f, indent=4)

# Carregar cardápio ao iniciar o programa
carregarCardapio()

# Função para validar o nome do cliente
def validarNome(nome):
    if not nome.strip():
        return False
    if any(char.isdigit() for char in nome):
        return False
    return True

# Função para adicionar novo item ao cardápio 
def adicionarItem():
    especificacao = input("\nDigite o item que deseja adicionar ao cardápio:\n")
    valorProduto = float(input("Digite o valor do item:\n"))
    novoCod = max(codigos) + 1
    codigos.append(novoCod)
    esp.append(especificacao)
    preco.append(valorProduto)
    salvarCardapio()


# Início do programa
comecarPrograma = int(input("Iniciar novo pedido? - 0 | Configurações - 1 \n"))

if comecarPrograma == 0:
    comecarPrograma = True

    while comecarPrograma:
        nome = input("Digite seu nome:\n")
        while not validarNome(nome):
            print("Nome inválido. Digite novamente (não pode estar vazio ou conter números).")
            nome = input("Digite seu nome:\n")

        listaPedidos.append(nome)
        comecarCompra = True

        while comecarCompra:
            print("\nCardápio:")
            for n in range(len(codigos)):
                print(f"{codigos[n]} - {esp[n]} - R$ {preco[n]:.2f}")

            cod = int(input("\nDigite o código desejado:\n"))

            if (cod in codigos):
                posicao = codigos.index(cod)

                pedido.append(cod)
                pedido.append(esp[posicao])
                pedido.append(preco[posicao])

                quantidade = int(input("Digite a quantidade:\n"))
                pedido.append(quantidade)

                valorTotal = pedido[2] * quantidade
                pedido.append(valorTotal)
                listaPreco.append(valorTotal)
                total = sum(listaPreco)

                listaPedidos.append(pedido[:])
                pedido.clear()

                confirma = input("Deseja finalizar o pedido? (S/N)\n")
                if(confirma == "s" or confirma == "S"):
                    comecarCompra = False
                    comecarPrograma = False
                else:
                    print("Adicionar novo item:\n")
            else:
                print("Insira um código válido.\n")

        # Imprimir o pedido do cliente
        print(f"\nNome: {listaPedidos[0]}")
        print("Pedido:")
        for item in listaPedidos[1:]:
            print(f"  - Código: {item[0]}, Produto: {item[1]}, Preço: R${item[2]}, Quantidade: {item[3]}, Subtotal: R${item[4]:.2f}")
        print(f"Total a pagar: R${total:.2f}")

        # Cria um arquivo txt com o pedido
        with open(os.path.join(os.path.dirname(__file__), "pedido.txt"), "w") as arquivo:
            arquivo.write(f"Nome: {listaPedidos[0]}\n")
            arquivo.write("Pedido:\n")
            for item in listaPedidos[1:]:
                pedidosFeitos = f"  - Codigo: {item[0]}, Produto: {item[1]}, Preço: R${item[2]}, Quantidade: {item[3]}, Subtotal: R${item[4]:.2f}\n"
                arquivo.write(pedidosFeitos)
            arquivo.write(f"Total a pagar: R${total:.2f}")

# Menu de Configurações
elif comecarPrograma == 1:
    menuConfig = True

    while menuConfig:
        usuario = input("\nDigite o usuário:\n")
        senha = input("Digite a senha:\n")

        if usuario == "gz" and senha == "123":
            adicionarItem()
            sair = input("\nSair das configurações? (S/N)\n")
            if(sair == "S" or sair == "s"): 
                menuConfig = False
            else:
                print("Adicionar novo item\n")
        else:
            print("Usuário ou senha incorretos.")

else:
    print("Pedido encerrado.")
