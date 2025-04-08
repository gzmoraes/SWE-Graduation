# 9) Elaborar um programa que receba um número positivo e maior que zero, calcule e mostre: 
# a) o número digitado ao quadrado;
# b) a raiz quadrada do número digitado
import math

num1 = int(input("Digite um número positivo e maior que zero: "))

quadrado = num1 * num1 
raiz = math.sqrt(num1)

print(f'O número digitado ao quadrado: {quadrado}\n A raiz quadrada do número digitado: {raiz}')

