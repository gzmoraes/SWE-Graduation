# 11) Elaborar um programa que calcule a aceleração de um corpo em movimento conhecendo-se as velocidades inicial e final, e o intervalo de tempo medido (a = (v2 –v1)/∆t). 
# Exibir o resultado

velInicial = float(input("Qual a velocidade inicial? "))
velFinal = float(input("Qual a velocidade final? "))
tempo = float(input("Qual o intervalo de tempo medido? "))

aceleracao = (velFinal - velInicial) / tempo

print(f"A aceleração do corpo é de {aceleracao}")