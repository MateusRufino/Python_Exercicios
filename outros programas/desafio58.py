import random
lista = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numero = random.choice(lista)
escolhido = int(input('Tente acertar o numero inteiro de 0 a 10 = '))
while escolhido != numero:
    escolhido = int(input('Voce errou, escolha novamente de 0 a 10 = '))

print('Parabens, voce escolheu o numero correto = {}'.format(numero))
print('------------FIM------------')