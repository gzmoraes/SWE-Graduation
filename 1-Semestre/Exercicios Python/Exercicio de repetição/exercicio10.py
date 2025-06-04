# Elaborar um programa que contem uma lista com 15 elementos. Essa lista deve ser preenchida
# pelo usuário, porém não deve conter valores repetidos. Exibir no final a lista

lista = []
n = 0

while n < 15:
    valor = int(input(f"Digite o {n + 1}º valor: "))
    if valor not in lista:
        lista.append(valor)
        n += 1
    else:
        print("Valor repetido. Digite um número diferente.")

print(f"Lista final: {lista}")
