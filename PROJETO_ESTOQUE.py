#=======Projeto: Sistema de Controle de Estoque Simples==========
#Aluno: Hudson Bruno
#from PROJETO_ESTOQUE.data_base import carregar_dados
from data_base import salvar_dados, carregar_dados
PROJETO_ESTOQUE/
├── index.html        
├── data_base.py
├── PROJETO_ESTOQUE.py
└── estoque.json

#CADASTRO PRODUTO
def cadastrar_produto():
    # IMPERDIR CÓDIGO DUPLICADO - TO DO
    todos_os_dados_dos_produtos = carregar_dados()
    lista_de_codigos_dos_produtos = []
    for produto_um_por_um in todos_os_dados_dos_produtos:
        lista_de_codigos_dos_produtos.append(produto_um_por_um['codigo'])

    # CRIAR CÓDIGO AUTOMÁTICO --- TO DO
    quantidade_de_produtos = len(carregar_dados())
    codigo = quantidade_de_produtos +1


   # codigo = input('Digite o codigo do produto: ')
    nome = input('Digite o nome do produto: ')
    quantidade = int(input('Digite o quantidade do produto: '))
    while quantidade <= 0:
        print("ERROR: QUANTIDADE NÃO PODE SER MENOR OU IGUAL A ZERO!")
        quantidade = int(input('Digite o quantidade do produto: '))
    preco = float(input('Digite o valor do produto: '))
    while preco <= 0:
        print("ERROR: PREÇO DEVE SER MAIOR QUE ZERO!")
        preco = float(input('Digite o valor do produto: '))
#SOLUÇÃO PARA O CADASTRO PARAR DE SOBRESCREVER OS DADOS ANTIGOS
    produto = carregar_dados()
    produto.append(
        {
            'codigo': codigo,
            'nome': nome,
            'quantidade': quantidade,
            'preco': preco
        }
    )
    salvar_dados(produto)
    print("Produto cadastrado com sucesso!")

#LISTAR PRODUTOS
def listar_produtos():
    listar_produtos = carregar_dados()
    print("###### LISTA DE PRODUTOS ######")
    for produto in listar_produtos:
        print("O código do produto é:", produto['codigo'])
        print("Nome do produto:", produto['nome'])
        print("Quantidade do produto é:", produto['quantidade'])
        print("Preço do produto:", produto['preco'], "\n")

#ATUALIZAR ESTOQUE
def atualizar_estoque():
    atualizar_estoque = carregar_dados()

#REMOVER PRODUTO DO ESTOQUE
def remover_produto():
    remover_produto = carregar_dados()
    produto_para_deletar = input('Nome do produto a ser removido: ')
    for nome in remover_produto:
        if nome == produto_para_deletar:
            del remover_produto[nome]
            salvar_dados(remover_produto)
            print("Produto removido com sucesso!")


#OPÇÃO DE BAIXO ESTOQUE
def ver_produtos_baixo_estoque():
    ver_produtos_baixo_estoque = carregar_dados()
    print("###### ALERTA: PRODUTOS BAIXO ESTOQUE ######", "\n")
    for quantidade in ver_produtos_baixo_estoque:
            if int(quantidade['quantidade']) <= 5:
                print("Quantidade em estoque:", "\n", quantidade['nome'], "\n", [quantidade['quantidade']])


#MENU
def exibir_menu():
        opcao_desejada = 0
        while opcao_desejada != 6:
            print("===== SISTEMA DE ESTOQUE ======", "\n")
            print("1 - Cadastrar produto")
            print("2 - Listar produtos")
            print("3 - Atualizar estoque")
            print("4 - Remover produto")
            print("5 - Ver produtos com baixo estoque")
            print("6 - Sair", "\n")
            opcao_desejada = int(input("Digite sua opção: "))

            if opcao_desejada == 1:
                cadastrar_produto()
            elif opcao_desejada == 2:
                listar_produtos()
            #elif opcao_desejada == 3: - TO DO
                #atualizar_estoque()
            elif opcao_desejada == 4:
                remover_produto()
            elif opcao_desejada == 5:
                ver_produtos_baixo_estoque()


exibir_menu()

# 1. Entra na pasta (ajuste o caminho)
cd caminho/para/PROJETO_ESTOQUE

# 2. Prepara todos os arquivos para commit
git add .

# 3. Cria o commit com uma mensagem descritiva
git commit -m "feat: adiciona interface web do sistema de estoque"

# 4. Envia para o GitHub
git push








