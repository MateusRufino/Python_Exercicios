salario = int(input('Digite o seu salário = '))

if salario > 1250:
    aumento = salario * 1.1
    print('seu salário de {} com o aumento de 10% é {}'.format(salario, aumento))
else:
    aumento = salario * 1.15
    print('seu salário de {} com o aumento de 15% é {}'.format(salario, aumento))