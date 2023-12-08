casa = float(input('Digite o valor da casa = '))
salario = float(input('Diite o seu salário = '))
tempo = float(input('Digite o tempo que deseja parcelar = '))

mensal = casa / tempo / 12
porcentagem = salario * 0.3
print('O valor da prestação é de {:.2f}'.format(mensal))
if mensal > porcentagem:
    print('empréstimo negado, a mesalidade de {:.2f} excede 30% do seu salário que é {:.2f}'.format(mensal, porcentagem))

else: print('empréstimo aceito, 30% do seu salário que é {:.2f} é o suficiente para cobrir a mensalidade de {:.2f}'.format(porcentagem, mensal))