# 18) Elaborar um programa que leia o tempo de duração de um evento em uma fábrica expressa
#     em segundos e mostre-o expresso em horas, minutos e segundos.

segTotais = int(input("Digite a duração do evento em segundos: "))

horas = segTotais // 3600
resto = segTotais % 3600
minutos = resto // 60
segundos = resto % 60

print(f"O tempo do evento é: {horas} horas, {minutos} minutos e {segundos} segundos")
