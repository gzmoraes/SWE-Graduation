# 10) Elaborar um programa que dados dois lados de um triângulo retângulo calcule e exiba a 
# respectiva hipotenusa
import math
ladoA = float (input("Digite o lado A: "))
ladoB = float (input("Digite o lado B: "))

hipotenusa = math.hypot(ladoA, ladoB)

print(f'{hipotenusa}')
