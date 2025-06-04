# Elaborar um programa que lê um número inteiro entre 1 e 7 e exibe o dia da semana 
# correspondente. O programa deve repetir até que o usuário digite um número fora desse 
# intervalo, caso isso aconteça o algoritmo mostra uma mensagem informando “Número 
# inválido”.

dia = 0

while (dia >= 0 and dia < 8):
    dia = int(input('Digite um numero de 1 a 7: '))

    if(dia == 1):
        print('Domingo')
    elif(dia == 2):
        print('Segunda')
    elif(dia == 3):
        print('Terça')
    elif(dia == 4):
        print('Quarta')
    elif(dia == 5):
        print('Quinta')
    elif(dia == 6):
        print('Sexta')
    else:
        print('Sabado')

else:
    print('Programa encerrado')