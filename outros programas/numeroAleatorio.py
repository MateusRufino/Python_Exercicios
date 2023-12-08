import random
lista = (0, 1, 2, 3, 4, 5)
numero = random.choice(lista)
escolhido = int(input('Tente acertar o numero inteiro de 0 a 5 = '))
if numero == escolhido:
    print('Parabens, voce escolheu o numero correto = {}'.format(numero))
else:
    print('Infelizmente voce errou, o numero correto e = {}'.format(numero))
print('------------FIM------------')