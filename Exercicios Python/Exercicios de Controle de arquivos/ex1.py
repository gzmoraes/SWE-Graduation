#Cria um arquivo txt de 0 a 100
abrirArquivo = open(("crescente.txt"), "w")
for n in range (1, 101):
    abrirArquivo.write(f"{n};")
print("Concluido")
    






    