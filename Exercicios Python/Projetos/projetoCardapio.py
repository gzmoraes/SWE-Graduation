#Listas relacionada ao pedido
pedido = []
listaPedidos = []

#listas de setup
codigos = [100,101]
esp = ["Hot - Dog","refri"]
preco = [10,5]

#lista para armazenar o valor
listaPreco = []

#Inicio programa
comecarPrograma = input("iniciar novo pedido? (S/N)\n")

if(comecarPrograma == "s" or comecarPrograma == "S"):
    comecarPrograma = 1

    #Inicio pedido
    while(comecarPrograma == 1):
        nome = input("Digite seu nome:\n")
        
        listaPedidos.append(nome)
        comecarCompra = 1

        while(comecarCompra == 1):
            print("Cardapio | Código  | Preço\n" \
              "100      | Hot-dog | R$10,00\n" \
              "101      | Refri   | R$5,00")
            
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
        print(f"pedido: {listaPedidos}")
        print(f"total a pagar: {total}")

else: 
    print("Pedido encerrado")

