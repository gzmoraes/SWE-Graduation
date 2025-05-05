# Elaborar um programa para automatizar o caixa de uma lanchonete. Este programa deve ler o 
# código do item pedido, a quantidade e somar para calcular o valor a ser pago. O programa
# termina quando o código for 0 (zero). O cardápio da lanchonete é o seguinte

pedido = []
total = 0
codigo = -1  

print("Cardápio:")
print("100 - Cachorro Quente - R$ 3,50")
print("101 - Bauru simples   - R$ 3,80")
print("102 - Bauru c/ ovo    - R$ 4,50")
print("103 - Hamburguer      - R$ 4,70")
print("104 - Cheesburguer    - R$ 5,30")
print("105 - Refrigerante    - R$ 4,00")
print("Digite 0 para encerrar o pedido.")

while codigo != 0:
    codigo = int(input("Código do item: "))

    if codigo != 0:
        quantidade = int(input("Quantidade: "))

        if codigo == 100:
            total =+ 3.50 * quantidade
            pedido.append(total)
        elif codigo == 101:
            total =+ 3.80 * quantidade
            pedido.append(total)
        elif codigo == 102:
            total =+ 4.50 * quantidade
            pedido.append(total)
        elif codigo == 103:
            total =+ 4.70 * quantidade
            pedido.append(total)
        elif codigo == 104:
            total =+ 5.30 * quantidade
            pedido.append(total)
        elif codigo == 105:
            total =+ 4.00 * quantidade
            pedido.append(total)
        else:
            print("Código inválido.")

pagar = sum(pedido)

print(pedido)
print(f"Total a pagar: R$ {pagar:.2f}")
