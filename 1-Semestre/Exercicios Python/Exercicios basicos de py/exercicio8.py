# 8) Elaborar um programa que dados o tamanho de um arquivo (em bits), bem como a velocidade  da conexão (em bits por segundo), informe o tempo necessário para o download do arquivo

tamArquivo = float(input("Qual o tamanho do arquivo que deseja fazer dowload? (Em bits)"))
velocidade = float(input("Qual a sua velocidade de conexão? (Em bits p/seg)"))

tempo = tamArquivo / velocidade

print (f'o tempo necessário para o dowload será de: {tempo}') 