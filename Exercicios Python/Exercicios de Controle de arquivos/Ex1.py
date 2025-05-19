abrirArquivo = open(("crescente.txt"), "w")
for n in range (1, 101):
    abrirArquivo.write(f"{n};")
print("Concluido")
