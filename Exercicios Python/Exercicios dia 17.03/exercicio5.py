#5) Elaborar um programa que leia o saldo de uma aplicação e imprimir o novo saldo, considerando 
#um reajuste de 15%.

saldo = int(input("Insira o valor do seu saldo:"))

novoSaldo = saldo + (saldo * 0.15)

print(f'O seu saldo atual é de {novoSaldo}')