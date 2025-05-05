# Elaborar um programa que lê um número N inteiro maior que 2 (caso N não for maior que 2 
# deve solicitar outro número). Logo após o programa deve exibir o quadrado e o cubo de 2 até N

n = 0
while n <= 2:
    n = int(input("Digite um número inteiro maior que 2: "))
    if n <= 2:
        print("Número inválido. Tente novamente.")
i = 2
print("\nNúmero  Quadrado  Cubo")
while i <= n:
    quadrado = i * i
    cubo = i * i * i
    print(f"{i:<8} {quadrado:<9} {cubo}")
    i = i + 1

    
