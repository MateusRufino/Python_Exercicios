primo = int(input('Digte o numero = '))
tot = 0
for c in range(1, primo + 1):
    if primo % c == 0:
        print('\033[34m', end=' ')
        tot = tot + 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')
print('\n O numero {} foi divisivel {} vezes'.format(primo, tot))

if tot == 2:
    print('o numero {} e primo'.format(primo))
else:
    print('o numero {} nao e primo'.format(primo))