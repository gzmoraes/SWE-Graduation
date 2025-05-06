#Listas relacionada ao pedido
pedido = []
listaPedidos = []

#listas de setup
codigos = [100,101,102,103,104,105]
esp = ["Cachorro Quente","Bauru Simples","Bauru c/Ovo","Hamburguer","Cheesburguer","Refrigerante"]
preco = [3.50,3.80,4.50,4.70,5.30,4]

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
    comecarPrograma = 1

    #Inicio pedido
    while(comecarPrograma == 1):
        nome = input("Digite seu nome:\n")
        while not validar_nome(nome):
            print("Nome inválido. Digite novamente (não pode estar vazio ou conter números).")
            nome = input("Digite seu nome:\n")

        listaPedidos.append(nome)
        comecarCompra = 1

        while(comecarCompra == 1):
            print("Cardápio:")
            print("100 - Cachorro Quente - R$ 3,50")
            print("101 - Bauru simples   - R$ 3,80")
            print("102 - Bauru c/ ovo    - R$ 4,50")
            print("103 - Hamburguer      - R$ 4,70")
            print("104 - Cheesburguer    - R$ 5,30")
            print("105 - Refrigerante    - R$ 4,00")
            
            cod = int(input("Digite o codigo desejado:\n"))
            
            #Se o cod informado estiver na lista ele prosegue e atribui os valores especificados daquele cod
            if(cod in codigos):
                continuaCompra = 1

                while(continuaCompra == 1):
                    if(cod == 100):
                        pedido.append(cod)
                        pedido.append(esp[0])
                        pedido.append(preco[0])
                        continuaCompra = 0
                    elif(cod == 101):
                        pedido.append(cod)
                        pedido.append(esp[1])
                        pedido.append(preco[1])
                        continuaCompra = 0
                    elif(cod == 102):
                        pedido.append(cod)
                        pedido.append(esp[2])
                        pedido.append(preco[2])
                        continuaCompra = 0
                    elif(cod == 103):
                        pedido.append(cod)
                        pedido.append(esp[3])
                        pedido.append(preco[3])
                        continuaCompra = 0
                    elif(cod == 104):
                        pedido.append(cod)
                        pedido.append(esp[4])
                        pedido.append(preco[4])
                        continuaCompra = 0
                    else:
                        pedido.append(cod)
                        pedido.append(esp[5])
                        pedido.append(preco[5])
                        continuaCompra = 0

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
                    comecarCompra = 0
                    comecarPrograma = 0
                    cod = 0

                else:
                    print("adicionar novo item:\n")

            else:
                print("Insira um valor valido\n")
            

        #Imprimir ao usuario seu pedido
        print(f"Nome: {listaPedidos[0]}")
        print("pedido:")
        for item in listaPedidos[1:]:
            print(f"  - Código: {item[0]}, Produto: {item[1]}, Preço: R${item[2]}, Quantidade: {item[3]}, Subtotal: R${item[4]}")
        print(f"Total a pagar: R${total}")

else: 
    print("Pedido encerrado")
