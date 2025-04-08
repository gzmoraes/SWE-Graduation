#4) Elaborar um programa que calcule o consumo médio de um automóvel (medido em km/l), dado que são conhecidos a distância total percorrida e o volume de combustível 
# consumido para percorrê-la (medido em litros)

kmPercorrido = int(input("Insira o Km percorrido:"))
combustivelGasto = int(input("Insira o combustivel gasto:"))

mediaKML = kmPercorrido / combustivelGasto

print(f'O consmoe médio foi de {mediaKML}km/l')
