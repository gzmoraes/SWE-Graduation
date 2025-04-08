# 15) Elaborar um programa que leia três números inteiros (A, B, C) e calcule a seguinte expressão: 

numA = int(input("Digite o primeio numero: "))
numB = int(input("Digite o segundo numero: "))
numC = int(input("Digite o terceiro numero: "))

R = (numA + numB)**2 
S = (numB + numC)**2
D = (R + S)/2

print(f'O valor de D é de: {D}')
