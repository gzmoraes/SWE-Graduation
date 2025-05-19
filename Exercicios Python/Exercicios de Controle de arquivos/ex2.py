#Cria um arquivo txt de 100 a 0
abrirArquivo = open(("decrescente.txt"), "w")
for n in range (100, 0, -1):
    abrirArquivo.write(f"{n};")
print("Concluido")