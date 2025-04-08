# 12) Elaborar um programa que receba o raio de uma esfera. O algoritmo deve calcular e exibir a área e o volume da esfera

raio = float(input("Qual o valor do raio da esfera? "))

area = 4 * 3.14 * (raio**2)
volume = (4/3) * 3.14 * (raio**3)



print(f"O volume da esfera é {volume}.\nA área da esfera é {area}")
