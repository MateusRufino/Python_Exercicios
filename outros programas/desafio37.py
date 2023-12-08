import math
numero = int(input('Digite o número que deseja converter = '))

escolha = int(input('Digite 1 para binário, 2 para octual, 3 para hexadecimal'))

if escolha == 1:
    print('o número convertido ficaria {}'.format(bin(numero)[2:]))

elif escolha == 2:
    print('o número convertido ficaria {}'.format(oct(numero)[2:]))

elif escolha == 3:
    print('o número convertido ficaria {}'.format(hex(numero)[2:]))