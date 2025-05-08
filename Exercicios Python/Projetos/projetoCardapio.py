#Listas relacionada ao pedido
pedido = []
listaPedidos = []

#listas de setup
codigos = [100,101,102,103,104,105]
esp = ["Cachorro Quente","Bauru Simples","Bauru c/Ovo","Hamburguer","Cheesburguer","Refrigerante"]
preco = [10,5,6.50,13.50,12,5]

#lista para armazenar o valor
listaPreco = []

# Função para validar o nome
def validar_nome(nome):
    if not nome.strip():
        return False
    if any(char.isdigit() for char in nome):
        return False
    return True

#Inicio programa
comecarPrograma = input("iniciar novo pedido? (S/N)\n")

if(comecarPrograma == "s" or comecarPrograma == "S"):
    comecarPrograma = True

    #Inicio pedido
    while(comecarPrograma == True):
        nome = input("Digite seu nome:\n")
        while not validar_nome(nome):
            print("\nNome inválido.\nDigite novamente (não pode estar vazio ou conter números).\n")
            nome = input("Digite seu nome:\n")

        listaPedidos.append(nome)
        comecarCompra = True

        while(comecarCompra == True):
            print("\nCardápio:")
            
            for n in range(len(codigos)):
                print(f"{codigos[n]} - {esp[n]} - R$ {preco[n]:.2f}")
            
            cod = int(input("\nDigite o codigo desejado:\n"))
            
            if(cod in codigos):
                posicao = codigos.index(cod)

                #Usa a posião do codigo para atribuir o resto das informações ao pedido
                pedido.append(cod)
                pedido.append(esp[posicao])
                pedido.append(preco[posicao])

                #Pergunta ao usuario a quantidade do item
                quantidade = int(input("Digite a quantidade:\n"))
                pedido.append(quantidade)

                #Realiza o calculo para saber quanto o cliente deve pagar
                valorTotal = pedido[2] * quantidade
                pedido.append(valorTotal)
                listaPreco.append(valorTotal)
                total = sum(listaPreco)

                #Atribui os itens na lista de pedido e apaga a lista pedido para que possa ser preechida com novos itens
                listaPedidos.append(pedido[:])
                pedido.clear()

                #Pergunta ao usuario se o pedido acabou
                confirma = input("Deseja finalizar o pedido? (S/N)\n")

                if(confirma == "s" or confirma == "S"):
                    comecarCompra = False
                    comecarPrograma = False

                else:
                    print("adicionar novo item:\n")

            else:
                print("Insira um valor valido\n")
            

        #Imprimir ao usuario seu pedido
        print(f"\nNome: {listaPedidos[0]}")
        print("pedido:")
        for item in listaPedidos[1:]:
            print(f"  - Código: {item[0]}, Produto: {item[1]}, Preço: R${item[2]}, Quantidade: {item[3]}, Subtotal: R${item[4]}")
        print(f"Total a pagar: R${total}")

else: 
    print("Pedido encerrado")
