ano = int(input('Digite o ano que deseja verificar se é bisexto = '))
resto = ano % 4
if resto == 0:
    print('O ano {} é um ano Bisexto!'.format(ano))

else:
    print('O ano {} não é um ano Bisexto!'.format(ano))