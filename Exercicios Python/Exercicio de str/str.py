
#1) Elaborar um programa que leia um nome e imprima as 4 primeiras letras do nome.
nome=input("Digite seu nome:\n")
 
print(nome[:4])

#2) Elaborar um programa que leia um nome e imprima o nome somente se a primeira letra do nome for “a” (maiúscula ou minúscula).
nome=input("Digite seu nome:\n")
if nome[0].lower() == "a":
    print(nome)


#3) Elaborar um programa que receba uma palavra ou texto e a imprima de trás-para-frente.
nome=input("Digite uma palavra ou texto:\n")
print(nome[::-1])


#4) Elaborar um programa que receba do usuário uma string. O programa deve imprimir a string sem suas vogais.
nome=input("Digite uma string:\n")
vogais = "aeiouAEIOU"
for i in vogais:
    nome = nome.replace(i, "")
 
print(nome)


#5) Elaborar um programa que receba uma palavra e calcule quantas vogais (a, e, i, o, u) possui essa palavra. Depois o usuário deve digitar um caractere (vogal ou consoante) e o programa deve substituir todas as vogais da palavra dada por esse caractere.
nome=input("Digite uma palavra:\n")
vogais = "aeiouAEIOU"
cont = 0
for i in nome:
    if i in vogais:
        cont += 1
print(f"A palavra possui {cont} vogais.")
substituto = input("Digite um caractere:\n")
for i in vogais:
    nome = nome.replace(i, substituto)
print(nome)


#6) Elaborar um programa que o usuário deve preencher uma lista com os modelos de cinco carros. O usuário também deve preencher outra lista com o consumo desses carros, isto é, quantos quilômetros cada um deles faz com um litro de combustível. Calcule e mostre:

#(a) O modelo de carro mais econômico;
 
#(b) Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1.000 quilômetros.
carros = []
consumo = []
for i in range(5):
    carro = input("Digite o modelo do carro:\n")
    carros.append(carro)
    cons = float(input("Digite o consumo do carro:\n"))
    consumo.append(cons)
 
economico = min(consumo)
indice = consumo.index(economico)
print(f"O carro mais economico é {carros[indice]} com {economico} km/l.")
for i in range(5):
    print(f"{carros[i]} consome {1000/consumo[i]} litros para percorrer 1000 km.")


#7) Elaborar um programa que, dada uma string, diga se ela é um palíndromo ou não. Lembrando que um palíndromo é uma palavra que tenha a propriedade de poder ser lida tanto da direita para a esquerda como da esquerda para a direita (Exemplo: ovo, arara).
def palindromo(string):
    return string == string[::-1]
string = input("Digite uma string:\n")
if palindromo(string):
    print("A string é um palíndromo.")
else:
    print("A string não é um palíndromo.")
    def palindromo(string):
        return string == string[::-1]
string = input("Digite uma string:\n")
if palindromo(string):
    print("A string é um palíndromo.")
else:
    print("A string não é um palíndromo.")