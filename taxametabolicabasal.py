peso = int(input('Qual o seu peso atual? '))
altura = int(input('Qual a sua altura atual em centimetros ?'))
idade = int(input('Qual a sua idade atual ? '))

taxametabolica = 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade)

print('Sua taxa metabolica basal é de {}'.format(taxametabolica))