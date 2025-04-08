#4) Um produto vai sofrer aumento de acordo com a tabela abaixo. Elaborar um programa que leia
#   o preço antigo, calcule e mostre o preço novo, e mostre uma mensagem em função do preço
#   novo (de acordo com a segunda tabela)

precoAntigo = float(input("Digite o valor antigo: "))


if (precoAntigo <= 50):
    precoNovo = precoAntigo + (precoAntigo * 0.05)
elif (precoAntigo > 50 and precoAntigo <= 100):
    precoNovo = precoAntigo + (precoAntigo * 0.10)
else:
    precoNovo = precoAntigo + (precoAntigo * 0.15)

if (precoNovo <= 80):
    print (f"Preço novo:{precoNovo}\n Barato")
elif (precoNovo > 80 and precoNovo <= 120):
    print (f"Preço novo:{precoNovo}\n Normal")
elif (precoNovo > 120 and precoNovo <= 200):
    print(f"Preço novo:{precoNovo}\n Caro")
else:
    print(f"Preço novo:{precoNovo}\n Muito caro")