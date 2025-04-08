pedido = [0,1,2,3,4]
esp = ["Hot-Dog","X-Burger","X-Egg","X-Tudo","Refri","Água"]
preco = [20,28,32,40,8,5]

novoPedido = input("Novo Pedido? (S/N) ")

if(novoPedido == "S" or novoPedido == "s"):
  pedido[0] = input("Digite o nome do cliente: ")

  print("\ncodigo | Cardapio  | valor unitário\n" \
  "1        Hot-Dog        R$20,00\n" \
  "2        X-Burguer      R$28,00\n" \
  "3        X-Egg          R$32,00\n" \
  "4        X-Tudo         R$40,00\n" \
  "5        Refri          R$8,00\n" \
  "6        Água           R$5,00\n")

  cod = int(input("Escolha o código do seu pedido: "))
  cod = cod - 1

  if(cod >= 0 and cod < 6):
    qnd = int(input("Insira a quantidade: "))
 
    nome = esp[cod]
    valor = preco[cod] 
    valorTotal = valor * qnd

    pedido[1] = nome
    pedido[2] = valor
    pedido[3] = qnd
    pedido[4] = valorTotal 

    print(f"Cliente: {pedido[0]}")
    print(f"Pedido: {pedido[1]}")
    print(f"Valor: {pedido[2]} reais")
    print(f"Quantidade: {pedido[3]}")
    print(f"Valor à pagar: {pedido[4]} reais")

    confirma = input("Confirmar pedido? (S/N) ")

    if(confirma == "S" or confirma == "s"):
      print("Pedido Finalizado!")
    else:
      print("Pedido Cancelado!")

  else:
    print("Codigo invalido")
 
else:
  print("Pedido cancelado!")

