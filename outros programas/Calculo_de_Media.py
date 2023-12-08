n1 = float(input('Digite a primeira nota = '))
n2 = float(input('Digite a segunda nota = '))
media = (n1 + n2) / 2

if media >= 7:
    print('Sua média foi {}{}{}, aprovado'.format('\033[4;32m', media, '\033[m'))

elif media < 5:
    print('Sua média foi {}{}{}, reprovado'.format('\033[4;32m', media, '\033[m'))

elif media < 6.9:
    print('sua média foi {}{}{}, está de recuperação'.format('\033[4;32m', media, '\033[m'))