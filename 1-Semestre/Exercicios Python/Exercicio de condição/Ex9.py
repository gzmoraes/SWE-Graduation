valor = float(input("Digite o valor do produto: "))
pagamento = int(input("Digite a forma de pagamento: (1 = A vista em dinheiro ou em cheque | 2 = A vista no cartão de crédito | 3 = Em duas vezes | 4 = Em mais de duas vezes): "))

if (pagamento == 1):
    desconto = valor * 0.10 
    pagar = valor - desconto
    print(f"Você recebeu 10 por cento de desconto! O valor da compra é de {pagar}")
elif (pagamento == 2):
    desconto = valor * 0.15 
    pagar = valor - desconto
    print(f"Você recebeu 15 por cento de desconto! O valor da compra é de {pagar}")
elif (pagamento == 3):
    pagar = valor / 2
    print(f"você pagara em duas vezes de {pagar}")
elif (pagamento == 4):
    juros = valor * 0.10
    pagar = valor + juros
    print(f"Você recebeu 10 por cento de juros! O valor da compra é de {pagar}")    
else:
    print("Escolha uma forma de pagamento valida!")