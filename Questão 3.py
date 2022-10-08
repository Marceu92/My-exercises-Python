print('Bem vindo ao programa de Feijoada do Marcéu - RU4194068')
volume = 0
acomp = 0
opcao = 0

# Função Valor para Volume
def volumeFeijoada():
    while True:

        global valor_volume #recebe o valor do volume selecionado

        try:
            print('Menu do volume da Feijoada')
            volume = int(input('Digite o volume da porção (ml) de feijoada desejada: '))  #recebe o volume da porção desejada
        except ValueError:
            continue
        if volume > 0:
            if volume < 300:
                print('Não são aceito volumes menores que 350ml ou maiores que 5L. Insira novamente um valor!')
            elif volume >= 300 and volume <= 5000:
                valor_volume = volume * 0.08
                break
            else:
                print('Não são aceito volumes menores que 350ml ou maiores que 5L. Insira novamente um valor!')
        continue

# Função Acompanhamento para Valor
def opcaoFeijoada():

    global opcao_valor  #recebe a multiplicação da variável globa valor_volume pela opção selecionada

    while True:
        print('Opções de Feijoadas')
        print('b - Básica (Feijão + paiol + costelinha)')
        print('p - Premium (Feijão + paiol + costelinha + partes de porco)')
        print('s - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)')
        opcao = input('Digite uma opção de porção de Feijoada: ')
        if opcao == 'b' or opcao == 'p' or opcao == 's':
            if opcao == 'b':
                opcao_valor = valor_volume * 1.00
                break
            elif opcao == 'p':
                opcao_valor = valor_volume * 1.25
                break
            elif opcao == 's':
                opcao_valor = valor_volume * 1.50
                break
        else:
            print('Opção digitada inválida, entre com uma opção válida')
            continue

# Função Valor para Acompanhamento
def acompanhamentoFeijoada():

    global acomp_preco  #recebe a soma dos preços dos acompanhamentos
    preco = 0   #contador de preço dos acompanhamentos

    while True:
        try:
            print('Opções de Acompanhamentos')
            print('0- Não desejo mais acompanhamentos (encerrar pedido)')
            print('1- 200g de arroz')
            print('2- 150g de farofa especial')
            print('3- 100g de couve cozida')
            print('4- 1 laranja descascada')
            acomp = int(input('>>> '))  #recebe opção de acompanhamento
        except ValueError:
            continue
        if acomp >= 0 and acomp <= 4:
            if acomp == 0:
                print('Não desejo mais acompanhamento (encerrar pedido)')
                break
            if acomp == 1:
                preco += 5
            if acomp == 2:
                preco += 6
            if acomp == 3:
                preco += 7
            if acomp == 4:
                preco += 3
        else:
            print('Opção inválida')
        continue
    acomp_preco = preco

# Programa Principal
volumeFeijoada()   #realiza o chamado da função valor
opcaoFeijoada()   #realiza o chamado da função opção_feijoada
acompanhamentoFeijoada()   #realiza o chamado da função acomp_feij

print('O total a ser pago é de R$ {:.2f}'.format(opcao_valor + acomp_preco))


