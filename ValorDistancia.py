distancia = int(input('Digite a distância a ser percorrida em km? = '))

if distancia <= 200:
    preco1 = distancia * 0.50
    print('Você percorreu {} km, deverá pagar R$ {}'.format(distancia, preco1))

else:
    preco2 = distancia * 0.45
    print('Você percorreu {} km, deverá pagar R$ {}'.format(distancia, preco2))