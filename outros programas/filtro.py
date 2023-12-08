somaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for p in range(1, 5):
    print('-------{} pessoa--------'.format(p))
    nome = str(input('nome = ')).strip()
    idade = int(input('idade = '))
    sexo = str(input('Sexo[M/F] = ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
print('A media da idade e igual a {}'.format(somaidade / 4))
print('O homem mais velho tem {} anos e seu nome e {}'.format(maioridadehomem, nomevelho))
print('ao todo {} mulheres tem mais de 20 anos'.format(totmulher20))
