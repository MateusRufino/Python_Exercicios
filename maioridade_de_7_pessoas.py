from _datetime import date
atual = date.today().year
cont1 = 0
cont2 = 0
for pess in range(1, 8):
    nasc = int(input('informe a {} pessoa nasceu = '.format(pess)))
    idade = atual - nasc

    if idade >= 21:
        cont1 += 1

    else:
        cont2 += 1
print('{} pessoas sao maiores de 21 anos e {} pessoas sao menores'.format(cont1, cont2))
