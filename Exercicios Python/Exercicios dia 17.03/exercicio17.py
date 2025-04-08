# 17) Elaborar um programa que leia a idade de uma pessoa expressa em anos, meses e dias e
#     mostre-a expressa apenas em dias.

anos = int(input("Digite a idade em anos: "))
meses = int(input("Digite a idade em meses: "))
dias = int(input("Digite a idade em dias: "))


idadeEmDias = (anos * 365) + (meses * 30) + dias
print(f"A idade expressa em dias é: {idadeEmDias} dias")


