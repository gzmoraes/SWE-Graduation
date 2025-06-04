# Elaborar um programa que solicite ao usuário vários valores inteiros. Quando o usuário digitar 
# o número 100 o programa deve terminar, mostrando quantos valores foram acima de 80,
# quantos foram abaixo de 10 e mostrar a média de todos os valores digitados pelo usuário.

lista = []
lista80 = []
lista10 = []

n = 0

while(n != 100):
    n = int(input('Digite um valor inteiro: '))
    
    if(n >= 80):
        lista80.append(n)
    elif(n <= 10):
        lista10.append(n)
    else:
        lista.append(n)

else:
    itens80 = len(lista80) 
    itens10 = len(lista10)
    itens = len(lista)

    soma = (sum(lista) + sum(lista10) + sum(lista80) - 100)
    media = soma / ((itens + itens10 + itens80) - 1)


    print(lista)
    print(lista10)
    print(lista80)
    print(soma)
    print(f'itens acima de 80: {itens80}\nitens abaixo de 10: {itens10}\nA média de todos os valores digitados: {media}')
