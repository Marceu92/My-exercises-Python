print('Bem vindo a loja do Marcéu - RU4194068 \n') #identificador pessoal
val_unit = float(input('Digite o valor do produto: ')) #recebe valor da unidade.
quant = int(input('Digite a quantidade de produto: ')) #recebe quantidade.

# Para representar o desconto é utilizada a variável 'desc'.
if quant <= 4:
    desc = 0        # não houve desconto na unidade
elif quant >= 5 and quant <= 19:
    desc = val_unit * 0.03      # desconto de 3% na unidade
elif quant >= 20 and quant <= 99:
    desc = val_unit * 0.06      # desconto de 6% na unidade
else:       # se o valor igual o  maior que 100 entra nesse else (quant >= 100)
    desc = val_unit * 0.1       # desconto de 10% na unidae

print('\nValor sem desconto foi: R$ {:.2f}'.format(val_unit*quant))
print('Valor com desconto foi: R$ {:.2f}'.format((val_unit-desc)*quant))

