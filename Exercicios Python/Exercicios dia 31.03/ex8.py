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
    resultado = (num1 + 2 * num2 + num3) / 6
    print(f"O resultado dessa operação é {resultado}")
elif (menu == "c"):
    resultado = ((1 / num1) + (1 / num2) + (1 / num3)) / 1
    print(f"O resultado dessa operação é {resultado}")
elif (menu == "d"):
    resultado = (num1 + num2 + num3) / 3
    print(f"O resultado dessa operação é {resultado}")
else:
    print("Opção inválida")