# 7) Elaborar um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre: 
# - A idade desta pessoa hoje;
# - A idade desta pessoa em 2035

nascimento = int(input("Em qual ano você nasceu?"))
anoAtual = int(input("Qual o ano atual?"))

idade = anoAtual - nascimento
idadeFutura = 2035 - nascimento

print(f"Você tem {idade} anos.\nEm 2035 você terá {idadeFutura} anos.")