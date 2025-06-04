def validarNome(nome):
    if not nome.strip():
        return False
    if any(char.isdigit() for char in nome):
        return False
    return True

def cadastroAlundos():
    nomeAluno = input("Digite o Nome do Aluno:\n")
    while not validarNome(nomeAluno):
        print("Nome inválido. Digite novamente (não pode estar vazio ou conter números).")
        nomeAluno = input("Digite seu nome:\n")
    cursoAluno = input("Digite o Curso:\n")
    email = nomeAluno.replace(" ", "") + "@escola.br"
    with open("listaAlunos.txt", "a") as listaAlunos:
        listaAlunos.write(f"{nomeAluno} | {email} | Curso:{cursoAluno}\n")
    print(f"{nomeAluno} | {email} | Curso:{cursoAluno}")
    sair = int(input("Sair? Sim = 1 | Não = 2\n"))
    return not sair == 1


def buscarAluno():
    buscar = input("Digite o Aluno que deseja buscar:\n")
    encontrado = False
    with open("listaAlunos.txt", "r") as listaAlunos:
        for linha in listaAlunos:
            if buscar in linha:
                print("Encontrado:", linha.strip())
                encontrado = True
    if not encontrado:
        print("Nome não encontrado")

def removerAluno():
    buscar = input("Digite o Aluno que deseja remover:\n")
    with open("listaAlunos.txt", "r") as listaAlunos:
        linhas = listaAlunos.readlines()
    with open("listaAlunos.txt", "w") as listaAlunos:
        listaAlunos.writelines([linha for linha in linhas if buscar not in linha])
    print(f"Linhas com '{buscar}' removidas.")

print("1 - Cadastrar Aluno")
print("2 - Lista de Alunos cadastrados")
print("3 - Buscar Aluno")
print("4 - Remover aluno\n")
menu = int(input("Escolha a Opção Desejada:\n"))
comecarPrograma = True

while comecarPrograma:
    if menu == 1:
        cadastro = True
        while cadastro:
            cadastro = cadastroAlundos()
        comecarPrograma = False
    elif menu == 2:
        with open("listaAlunos.txt", "r") as listaAlunos:
            print(listaAlunos.read())
        comecarPrograma = False
    elif menu == 3:
        buscarAluno()
        comecarPrograma = False
    elif menu == 4:
        removerAluno()
        comecarPrograma = False
    else:
        print("Insira um código válido\n")
        menu = int(input("Escolha a Opção Desejada:\n"))