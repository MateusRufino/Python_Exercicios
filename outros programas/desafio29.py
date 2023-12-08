velocidade = int(input("Qual velocidade o carro passou ="))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print("Você foi multado em R$ {}".format(multa))

else:
    print('você não foi multado')