# Elaborar um programa que solicita varias temperaturas em graus Celsius. Para cada 
# temperatura inserida, o programa deve converter para graus Fahrenheit e Kelvin e mostrar na 
# tela. O programa termina quanto a temperatura inserida for menor que -5. 

c = 0

while (c > -5):
    c = float(input('Digite a temperatura em C°: '))
    f = (c * (9/3)) + 32
    k = c * 273

    print(f"Celsius: {c}\nFahreinheit: {f}\nKelvin: {k}")
else:
    print('Programa encerrado')