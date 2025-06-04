# Elaborar um programa que contem uma lista com N elementos. Essa lista deve ser preenchida
# pelo usuário e só deve conter números inteiros positivos e pares. Caso o usuário digite o 
# número 1 a repetição termina. Exibir no final todos os elementos da lista

lista = []
n = 0

while n != 1:
    n = int(input("Digite um número positivo e par (1 para sair): "))

    if n != 1:
        if n > 0 and n % 2 == 0:
            lista.append(n)
        else:
            print("Número inválido. Apenas positivos e pares são permitidos.")

print("Lista final:", lista)
