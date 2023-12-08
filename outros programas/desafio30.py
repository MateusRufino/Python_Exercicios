import math
numero = int(input('Digite o número inteiro a ser verificado ?'))
resto = numero % 2
if resto == 1:
    print('O número {} é Impar'.format(numero))
else:
    print('O número {} é par'.format(numero))