def cadastroProduto():
    # Abre o arquivo de produtos para leitura
    produtos = open('produtos.txt','r')
    linha = produtos.readlines()
    produtos.close()

    # Listas para armazenar IDs e produtos já cadastrados
    listaId = [] 
    listaProdutos = []

    # Processa cada linha do arquivo e preenche as listas
    for i in linha:
        coluna = i.strip().split(';')
        idCol = int(coluna[0])
        listaId.append(idCol)
        nomeCol = coluna[1]
        valorCol = float(coluna[2].replace('R$','').strip())
        listaProdutos.append([idCol, nomeCol, valorCol])

    # Solicita os dados do novo produto
    nome = input('Digite o nome do produto:\n')
    valor = float(input('Digite o valor do produto:\n'))

    # Gera um novo ID baseado no maior ID existente
    if len(listaId) == 0:
        id = 1
    else:
        id = max(listaId) + 1
    
    # Adiciona o novo produto à lista
    listaProdutos.append([id, nome, valor])

    # Ordena os itens 
    listaProdutos.sort()

    # Abre o arquivo para reescrever
    produtos = open('produtos.txt','w')
    for produto in listaProdutos:
        produtos.write(f'{produto[0]};{produto[1]};R${produto[2]:.2f}\n')
    produtos.close()
    print('\nProduto Adicionado Com Sucesso!\n')


def buscarProduto():
    # Recebe o nome a ser buscado
    nome = input('Digite o nome do produto que deseja buscar:\n')

    # Lê todos os produtos do arquivo
    produtos = open('produtos.txt','r')
    linha = produtos.readlines()
    produtos.close()

    # Listas para armazenar os dados lidos
    listaId = [] 
    listaNome = []
    listaPreco = []

    # Processa cada linha e preenche as listas
    for i in linha:
        coluna = i.strip().split(';')
        idCol = int(coluna[0])
        nomeCol = coluna[1]
        valorCol = float(coluna[2].replace('R$','').strip())

        listaId.append(idCol)
        listaNome.append(nomeCol)
        listaPreco.append(valorCol)
    
    # Normaliza o nome digitado para facilitar a busca
    nome = nome.lower()
    encontrado = False

    # Verifica se algum nome contém a string digitada
    for i in range(len(listaNome)):
        if nome in listaNome[i].lower():
            id = listaId[i]
            nomeProd = listaNome[i]
            valor = listaPreco[i]

            print(f'ID: {id} | Nome: {nomeProd} | Valor: R${valor:.2f}')
            encontrado = True

    # Se nada for encontrado
    if encontrado == False:
        print('Produto não encontrado')


def valorTotal():
    # Lê todos os produtos do arquivo
    produtos = open('produtos.txt','r')
    linha = produtos.readlines()
    produtos.close()

    listaValor = []
    
    # Extrai os valores e soma todos
    for i in linha:
        coluna = i.strip().split(';')
        colValor = float(coluna[2].strip().replace('R$',""))
        listaValor.append(colValor)

    soma = sum(listaValor)
    print(f'O valor total dos produtos é: R${soma}')


def editarProduto():
    # Lê os dados do arquivo
    produtos = open('produtos.txt','r')
    linha = produtos.readlines()
    produtos.close()

    listaGeral = []

    # Recebe o ID do produto a ser alterado
    idp = input('Insira o ID do Produto que deseja alterar:\n')

    for i in linha:
        if idp in i:  
            novoNome = input('Digite o novo Nome:\n')
            novoValor = float(input('Digite o novo Valor:\n'))
            novaLinha = f'{idp};{novoNome};R${novoValor:.2f}\n'
            listaGeral.append(novaLinha)
        else:
            listaGeral.append(i)

    # Ordena a lista
    listaGeral.sort()

    # Reescreve todo o arquivo com as alterações
    produtos = open('produtos.txt','w')
    produtos.writelines(listaGeral)
    produtos.close()
    print('\nProduto Alterado com Sucesso!\n')


def listarProduto():
    # Lê o conteúdo do arquivo
    produtos = open('produtos.txt','r')
    listar = produtos.readlines()
    produtos.close()

    # Mostra os produtos um a um formatados
    for i in listar:
        coluna = i.strip().split(';')
        idCol = int(coluna[0])
        nomeCol = coluna[1]
        valorCol = float(coluna[2].strip().replace('R$',""))

        print(f'ID: {idCol} | Nome: {nomeCol} | Preço: R${valorCol:.2f}')

    
def apagarProduto():
    # Lê os dados do arquivo
    produtos = open('produtos.txt','r')
    linhas = produtos.readlines()
    produtos.close()

    # Solicita o ID do produto a ser excluído
    idp = int(input('Digite o ID do produto que deseja apagar:\n'))

    novaLista = []  # Lista que receberá os produtos que permanecerão

    encontrado = False

    for i in linhas:
        colunas = i.strip().split(';')
        idCol = int(colunas[0])
        nomeCol = colunas[1]
        valorCol = colunas[2]

        if idCol == idp:
            encontrado = True
            print('Produto excluído com sucesso!\n')
        else:
            novaLista.append(f'{idCol};{nomeCol};{valorCol}\n')

    # Reescreve o arquivo apenas com os produtos que sobraram
    produtos = open('produtos.txt', 'w')
    produtos.writelines(novaLista)
    produtos.close()

    if not encontrado:
        print('ID não encontrado.\n')

        
start = True

while start == True:
    print('\nEscolha a opção desejada:\n' \
    '\n1 - Cadastrar Produto\n' \
    '2 - Listar Produtos\n' \
    '3 - Editar Produtos\n' \
    '4 - Apagar Produto\n' \
    '0 - Sair\n') 

    escolha = int(input('Esolha uma Opção:\n'))
    
    if escolha == 1:
        cadastroProduto()
    elif escolha == 2:
        listarProduto()
    elif escolha == 3:
        editarProduto()
    elif escolha == 4:
        apagarProduto()
    elif escolha == 0:
        start = False
    else:
        print('Codigo incorreto! Digite novamente:\n')
        escolha = int(input('Esolha uma Opção:\n'))

