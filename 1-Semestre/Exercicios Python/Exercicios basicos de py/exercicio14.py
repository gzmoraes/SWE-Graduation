# Elaborar um programa que leia uma temperatura em graus Celsius e deve converter em graus 
# Fahrenheit. A fórmula de conversão é: F = (9*C+160)/5, sendo F a temperatura em Fahrenheit e C 
# a temperatura em Celsius. Exibir a temperatura em Fahrenheit.

celsius = int(input("Digite a temperatura(C°): "))

fahrenheit = (9 * celsius + 160) / 5

print(f'A temperatura em Fahrenheit é de {fahrenheit}F°')