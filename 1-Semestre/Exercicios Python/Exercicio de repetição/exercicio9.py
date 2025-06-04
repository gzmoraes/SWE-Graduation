# Elaborar um programa que contenha uma lista com 25 elementos em que o usuário deve 
# preencher com valores reais. Logo em seguida, deve ser solicitado ao usuário que digite dois 
# números. Esses números devem corresponder a posições na lista (caso contrário solicite um 
# novo valor). Após inserir os dois números o programa deve exibir a soma dos elementos das 
# duas posições da lista.

lista = []
i = 0

while i < 25:
    valor = float(input(f"Digite o {i + 1}º número: "))
    lista.append(valor)
    i += 1

p1 = -1
p2 = -1

# Continua pedindo até que ambas as posições sejam válidas
while p1 < 0 or p1 > 24 or p2 < 0 or p2 > 24:
    p1 = int(input("Digite a primeira posição (0 a 24): "))
    p2 = int(input("Digite a segunda posição (0 a 24): "))

    if p1 < 0 or p1 > 24 or p2 < 0 or p2 > 24:
        print("Posições inválidas. Tente novamente.")

soma = lista[p1] + lista[p2]
print(f"Soma dos valores nas posições {p1} e {p2}: {soma}")

