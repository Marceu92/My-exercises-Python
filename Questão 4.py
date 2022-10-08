codigo = 0      # Contador, utilizado na função cadastroProduto, responsável pela geração do vaor 'código' no dicionário 'produto'
produto = {}    # Dicionário que receberá os valores: código, nome, fabricante e valor
produtos = []   # Dicionário que recebe valores do Dicionário 'produto'

def cadastrarProduto():     # função que receberá os valores do dicionário 'produto' e com a função .append irá inserir os dicionários 'produto' em 'produtos'
    produto['Código:'] = '{:03}'.format(codigo)
    print('Código do produto {:03d}'.format(codigo))
    produto['Nome:'] = input('Qual o nome do produto?\n>>> ')
    produto['Fabricante:'] = input('Qual a sua fabricante?\n>>> ')
    while True:
        try:
            produto['Valor:'] = '%.2f' % float(input('Qual o seu valor?\n>>> '))
            break
        except ValueError:
            continue
    produtos.append(produto.copy())

def consultarProduto():     # função responsável pela consulta das chaves e valor contidas no dicionério 'produtos'
    while True:
        try:
            print('Opções de Consulta')
            print('1 - Consultar Produtos')
            print('2 - Consultar produtos por código')
            print('3 - Consultar produtos por fabricantes')
            print('4 - Votar')
            opcao_produto = int(input('>>> '))  # Recebe opção de consulta em produtos
        except ValueError:
            continue
        if opcao_produto >= 1 and opcao_produto <= 4:
            if opcao_produto == 1:  # Exibirá todos as listas dicionários no dicionário 'produtos'
                print('-'*30)
                for produto_produtos in produtos:
                    for chave, valor in produto_produtos.items():
                        print('{} {}'.format(chave, valor))
                print('-' * 30)
            elif opcao_produto == 2:    # Exibirá somente a lista de dicionário de acordo com o código inserido
                codigo = int(input('Qual o Código do Produto?\n>>> '))
                codigo = "{:03}".format(codigo)
                for codigo_produtos in range(len(produtos)):    # A função range(len(produtos)) será utilizada para limitar o loop de for a extensão do conteúde do dicionário 'produtos'
                    if codigo == produtos[codigo_produtos]['Código:']:
                        print('-' * 30)
                        for chave, valor in produtos[codigo_produtos].items():
                            print(chave, valor)
                        print('-' * 30)
            elif opcao_produto == 3:    # Exibirá somente a(s) lista(s) o(s) dicionário(s) de acordo com o fabricante
                fabricante = input('Qual o Fabricante?\n>>> ')
                for fabricante_produtos in range(len(produtos)):
                    if fabricante == produtos[fabricante_produtos]['Fabricante:']:
                        print('-' * 30)
                        for chave, valor in produtos[fabricante_produtos].items():
                            print(chave, valor)
                        print('-' * 30)
            elif opcao_produto == 4:
                break
        else:
            print('Opção inválida!!!')
            continue

def removerProduto():   # Função para remover lista de dicionário especifica de acordo com o seu código no dicionário 'produtos'
    remove = int(input('Qual o produto a ser removido?\n>>> '))  # Recebe o valor do 'código' do dicionário em 'produtos' a ser removido
    remove -= 1 # A variável 'remove' será subtraída por -1, pois a lista de dicionário inicia em 0
    if remove > 0 and remove <= codigo:
        produtos.pop(remove)
    else:
        print('Código inválido!!!')


#PROGRAMA PRINCIPAL

print('Programa de Cadastro de Produtos, Marcéu - RU4194068')
while True:
    try:
        print('Opções de Acompanhamento de Produto')
        print('1 - Cadastrar Produto')
        print('2 - Consultar Produto(s)')
        print('3 - Remover Produto')
        print('4 - Sair')
        opcao = int(input('>>> '))  # recebe opção de acompanhamento de produto
    except ValueError:
        continue
    if opcao >= 1 and opcao <= 4:
        if opcao == 1:
            codigo += 1
            cadastrarProduto()
        elif opcao == 2:
            consultarProduto()
        elif opcao == 3:
            removerProduto()
        elif opcao == 4:
            print('Fim do Programa...')
            break
    else:
        print('Opção inválida!!!')
    continue











