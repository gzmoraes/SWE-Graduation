#13) Elaborar um programa que receba o raio e a altura de uma lata de óleo para calcular e 
#apresentar o valor do volume desta lata, dado: V = π*r2*h

raio = float(input("Digite o raio da lata: "))
altura = float(input("Digite a altura da lata: "))

volume = 3.14 * (raio**2) * altura

print(f'O volume é de {volume}')

