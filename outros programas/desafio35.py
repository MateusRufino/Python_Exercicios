print('-='*20)
print('  Analisador de triângulos')
print('-='*20)
n1 = float(input('Reta 1 = '))
n2 = float(input('Reta 2 = '))
n3 = float(input('Reta 3 ='))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('As restas informadas podem formar um triângulo')

else:
    print('As retas informadas não podem formar um triãngulo')