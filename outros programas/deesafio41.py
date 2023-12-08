nas = int(input('Digite seu ano de nascimento para saber a categoria = '))
cat = 2023 -nas

if cat < 9:
    print('Você tem {} anos, sua categoria é a mirim'.format(cat))

elif cat < 14:
    print('Você tem {} anos, sua categoria é a infantil'.format(cat))

elif cat < 19:
    print('Você tem {} anos, sua categoria é a junior'.format(cat))

elif cat == 20:
    print('Você tem {} anos, sua categoria é a sênior'.format(cat))

elif cat > 20:
    print('Você tem {} anos, sua categoria é a master'.format(cat))
