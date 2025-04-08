# 19) Elaborar um programa que calcule o salário líquido de um funcionário, exibindo no final o nome,
# telefone e o salário líquido, considerando:
# a) os dados do funcionário: nome, RG e telefone.
# b) salário bruto de R$ 2500,00
# c) descontos de R$ 300,00

nome = input("Digite o nome do funcionário: ")
rg = input("Digite o RG do funcionário: ")
telefone = input("Digite o telefone do funcionário: ")

salarioBruto = 2500.00
descontos = 300.00
salarioLiquido = salarioBruto - descontos

print(f"Nome: {nome}")
print(f"Telefone: {telefone}")
print(f"Salário Líquido: R$ {salarioLiquido:.2f}")