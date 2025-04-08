# 6) Elaborar um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário

salario = int(input("Qual o seu salário atual?"))
percentual = int(input("Qual foi o percentual de aumento?"))

aumento = salario * (percentual / 100)
novoSalario = salario + aumento 

print(f"Seu salário aumentou R${aumento}.\nSeu salário atual é R${novoSalario}")