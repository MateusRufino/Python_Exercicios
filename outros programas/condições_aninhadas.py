nome = str(input('Qual é o seu nome? '))

print('é um prazer te conmhecer, {}!'.format(nome))
if nome == 'mateus':
    print('Que belo nome você tem {}'.format(nome))

elif nome == 'maria' or nome == 'João' or nome == 'pedro':
    print('Você tem um nome bem comum no brasil{}'.format(nome))

elif nome in 'ana jessica claudia roberta':
    print('Você tem um lindo nome feminino')

else: print('seu nome é normal {}'.format(nome))