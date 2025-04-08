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

print(f"O resultado dessa operação matemática é {resultado}")