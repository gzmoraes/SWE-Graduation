#2) Elaborar um programa que receba quatro números inteiros, que calcule e mostre a soma e a média desses números.

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
num3 = int(input("Digite o terceiro número:"))
num4 = int(input("Digite o quarto número:"))

resSoma = num1 + num2 + num3 + num4

resMedia = resSoma/4

print(f'A soma dos quatro numeros é de {resSoma}\n A Média é de {resMedia}')