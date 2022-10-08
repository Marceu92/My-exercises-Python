print('Bem vindo a Pizzaria do Marcéu - RU4194068')
print('----------------------CARDÁPIO----------------------')
print('| Código | Descrição  | Pizza Média | Pizza Grande |')
print('|   21   | Napolitana |    R$ 20,00 |     R$ 26,00 |')
print('|   22   | Margherita |    R$ 20,00 |     R$ 26,00 |')
print('|   23   | Calabresa  |    R$ 25,00 |     R$ 32,00 |')
print('|   24   | Toscana    |    R$ 30,00 |     R$ 39,00 |')
print('|   25   | Portuguesa |    R$ 30,00 |     R$ 39,00 |')

preco = 0       #acumulador de preço das pizzas

while True:
    tipo = input('Selecione o tamanho da Pizza (M/G): ')       #recebe tamanho da pizza: M ou G
    if tipo != 'M' and tipo != 'G':
        print('Opção inválida!')
        continue        #o 'continue' gera loop caso a entrada 'tipo' seja diferente das string: 'M' e 'G'

    codigo = int(input('Insira o código: '))        #recebe código referente a pizza
    if codigo > 20 and codigo < 26:
        if codigo == 21:
            print('Você pediu uma Pizza de Napolitano')
            if tipo == 'M':
                preco += 20.00      #somatória da variável acumuladora: preco += (valor referente a pizza)
            else:
                preco += 26.00
        elif codigo == 22:
            print('Você pediu uma Pizza de Margherita')
            if tipo == 'M':
                preco += 20.00
            else:
                preco += 26.00
        elif codigo == 23:
            print('Você pediu uma Pizza de Calabresa')
            if tipo == 'M':
                preco += 25.00
            else:
                preco += 32.00
        elif codigo == 24:
            print('Você pediu uma Pizza de Toscana')
            if tipo == 'M':
                preco += 30.00
            else:
                preco += 39.00
        else:
            print('Você pediu uma Pizza de Portuguesa')
            if tipo == 'M':
                preco += 30.00
            else:
                preco += 39.00
    else:
        print('Opção inválida!')
        continue        #o 'continue' gera loop caso a entrada 'codigo' seja diferente das entradas: 21,22,23,24,25

    print('Deseja pedir mais alguma coisa:','\n1.Sim','\n2.Não')
    novo = (input('>>> '))
    if novo == '1':
        continue        #o 'continue' gera loop caso a entrada 'novo' seja uma string diferente de '1'
    else:
        print('O valor total a ser pago: R${:.2f}'.format(preco))
        break       #o 'break' gera o encerramento caso a entrada 'novo' seja uma string diferente de '1', encerrando o programa e printando o valor total
print('Pedido encerrado!')


