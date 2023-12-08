nas = int(input('Digite o seu ano de nascimento = '))
idade = 2023 - nas
tempo = idade - 18
if idade == 18:
    print('Você tem {} anos, está na hora de se alistar'.format(idade))

elif idade > 18:
    print('Você tem {} anos, já passou da idade de se alistar'.format(idade))
    print('Você passou {} anos da idade de se alistar'.format(tempo))

else:
    print('Você tem {} anos, futuramente irá se alistar'.format(idade))
    print('ainda falta {} anos para você se alistar'.format(tempo))