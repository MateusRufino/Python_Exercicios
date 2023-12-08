n1 = int(input('Digite a primeira nota = '))
n2 = int(input('Digite a segunda nota = '))
m = (n1 + n2 ) / 2
if m >= 7:
    print('Voce foi aprovado com a media {}'.format(m))
else:
    print('Voce foi reprovado com a media {}'.format(m))
print('Agradescemos por participar do nosso concurso')