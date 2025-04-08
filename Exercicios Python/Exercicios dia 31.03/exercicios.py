#1) Elaborar um programa que leia a idade e o tempo de serviço de um trabalhador e mostre se o
#   trabalhador pode ou não se aposentar. As condições para aposentadoria são:
#    • Ter pelo menos 65 anos,
#    • Ou ter trabalhado pelo menos 30 anos,
#    • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input("Digite sua idade?: "))
tempoServico = int(input("Qual seu tempo de serviço?: "))

if(idade >= 65 or tempoServico >= 30):
    print("Você ja pode se aposentar!")
elif (idade >= 60 and tempoServico >= 25):
    print("Você ja pode se aposentar!")
else:
  print ("Você não pode se aposentar!")


#2) Elaborar um programa que leia a distancia em km e a quantidade de litros de gasolina
#   consumidos por um carro em um percurso, calcule o consumo em Km/l e mostre uma mensagem
#   de acordo com a tabela abaixo:

km = float(input("Digite a distância percorrida: (KM)"))
gasolina = float(input("Digite o consumo de gasolina utilizado: "))

kml = km / gasolina

if(kml <8):
    print ("Venda o carro!")
elif(kml >= 8 and kml <14):
    print("Econmico!")
else:
    print("Super Econômico!")

#3) Elaborar um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela
#   a seguir, verifique e mostra qual a classificação dessa pessoa.

altura = int(input("Digite sua altura: (Ex: 170)"))
peso = float(input("Digite seu peso: "))

if(altura < 120 and peso <= 60):
    print("Sua classificação é: A")
elif(altura < 120 and peso >= 60 and peso <= 90):
    print("Sua classificação é: D")
elif(altura < 120 and peso > 90):
    print("Sua classificação é: G")

elif(altura >= 120 and altura <= 170 and peso <= 60):
    print("Sua classificação é: B")
elif(altura >= 120 and altura <= 170 and peso >= 60 and peso <= 90):
    print("Sua classificação é: E")
elif(altura >= 120 and altura <= 170 and peso > 90):
    print("Sua classificação é: H")

elif(altura > 170 and peso <= 60):
    print("Sua classificação é: C")
elif(altura > 170 and peso >= 60 and peso <= 90):
    print("Sua classificação é: F")
elif(altura > 170 and peso > 90):
    print("Sua classificação é: I")

else:
    print("valor invalido")


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


# 5) Elaborar um programa para automatizar o caixa de uma lanchonete. Este algoritmo deve ler o
#    código do item pedido, a quantidade e calcular o valor a ser pago por aquele lanche. No final o
#    programa deve mostrar o total a ser pago. O cardápio da lanchonete é o seguinte:

codigo = int(input("\n100 - Cachorro Quente | R$3,50"
"\n101 - Bauru Simples | R$3,80"
"\n102 - Bauru c/ovo | R$4,50"
"\n103 - Hamburger | R$4,70"
"\n104 - cheseeburger | R$5,30"
"\n105 - Refrigerante | R$4,00\n\n"
"Qual o código do lanche/bebida que deseja pedir?"))
quantidade = int(input("Qual a quantidade que desaja consumir: "))

if(codigo == 100):
    pagar = 3.50
elif(codigo == 101):
    pagar = 3.80
elif(codigo == 102):
    pagar = 4.50
elif(codigo == 103):
    pagar = 4.70
elif(codigo == 104):
    pagar = 5.30
elif(codigo == 105):
    pagar = 4.00
else:
    print("Valor inválido") 

totalPagar = pagar * quantidade
print(f"O valor final do pedido é de R${totalPagar}")


# 6) Elaborar um programa que mostre ao usuário um menu com 4 opções de operações
#    matemáticas (1- soma, 2- subtração, 3- multiplicação e 4- divisão). Após o usuário escolher uma
#    das opções, o programa deve solicitar dois números e realiza a operação escolhida. Logo em
#    seguida, o programa deve mostrar qual foi conta realizada e qual o resultado.

operacao= int(input("\n1 - Soma"
"\n2 - Subtração"
"\n3 - Multiplicação"
"\n4 - Divisão\n\n"
"Qual operção matemática deseja realizar? "))

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

if(operacao == 1):
    resultado = num1 + num2
elif(operacao == 2):
    resultado = num1 - num2
elif(operacao == 3):
    resultado = num1 * num2
elif(operacao == 4):
    resultado = num1 / num2
else:
    print("Valor inválido")


# 7) Elaborar um programa que receba três valores (A, B, C). O programa deve verificar se eles
#    podem ser valores dos lados de um triângulo, e se forem, se é um triângulo escaleno, equilátero
#    ou isóscele, considerando os seguintes conceitos:
#    • O comprimento de cada lado de um triângulo é menor do que a soma dos outros
#    dois lados.
#    • Chama-se equilátero o triângulo que tem três lados iguais.
#    • Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
#    • Recebe o nome de escaleno o triângulo que tem os três lados diferentes.

A = float(input("Qual o valor de A? "))
B = float(input("Qual o valor de B? "))
C = float(input("Qual o valor de C? "))


if (A + B < C or C + B < A or A + C < B):
    print("Esses valores NAO podem ser um triângulo")
elif (A == B and A == C):
    print("Ele é um triângulo equilátero")
elif (A == B or A == C or B == C):
    print("Ele é um triangulo isósceles")
elif (A != B != C):
    print("Ele é um triangulo escaleno")


# 8) Elaborar um programa que leia três números inteiros positivos e efetue o cálculo de uma das
#    seguintes médias de acordo a letra digitada pelo usuário:

import math
menu = (input("\na - Geométrica"
"\nb - Ponderada"
"\nc - Harmônica"
"\nd - Aritmética\n\n"
"Qual operção matemática deseja realizar? "))

num1 = int(input("Insira o primeiro número, ele deve ser inteiro e positivo: "))
num2 = int(input("Insira o segundo número, ele deve ser inteiro e positivo: "))
num3 = int(input("Insira o terceiro número, ele deve ser inteiro e positivo: "))



if (menu == "a"):
    mult = num1 * num2 * num3
    resultado = pow(mult, 1/3)
    print(f"O resultado dessa operação é {resultado}")
elif (menu == "b"):
    resultado = (num1 + 2 * num2 + 3 * num3) / 6
    print(f"O resultado dessa operação é {resultado}")
elif (menu == "c"):
    resultado = ((1 / num1) + (1 / num2) + (1 / num3)) / 1
    print(f"O resultado dessa operação é {resultado}")
elif (menu == "d"):
    resultado = (num1 + num2 + num3) / 3
    print(f"O resultado dessa operação é {resultado}")
else:
    print("Opção inválida")

