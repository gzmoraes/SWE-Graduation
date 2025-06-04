# Elaborar um programa que deve ler N números. Caso o usuário digite zero (0), o programa 
# deve exibir a somatória e a média dos valores inseridos.

lista = []

n = 1

while(n > 0 or n < 0):
    n = int(input('Digite um número: (Digite 0 para encerrar o programa)'))
    lista.append(n)
else:
    print(lista)
    soma = sum(lista) 
    media = soma / (len(lista) - 1)
    print(f'A soma dos números é de {soma}\nA média é {media:.2f}')
