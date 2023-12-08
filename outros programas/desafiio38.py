v1 = int (input('Digite o primeiro valor = '))
v2 = int (input('diite o segundo valor = '))

if v1 > v2:
    print('O {}primeiro valor{} é maior'.format('\033[4;34m', '\033[m'))

elif v1 < v2:
    print('O {}segundo valor{} é maior'.format('\033[4;34m', '\033[m'))

else:
    print('{}Não existe{} valor maior, os dois são iguais'.format('\033[4;34m', '\033[m'))