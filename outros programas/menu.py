from time import sleep
n1 = int(input('Digite um valor = '))
n2 = int(input('Digite outro valor = '))
print('-=' * 20)
escolha = 0
while escolha != 5:
    escolha = int(input('\n Digite [1] para somar \n Digite [2] para multiplicar \n Digite [3] para maior \n Digite [4] para novos numeros \n Digite [5] para sair do programa \n Digite o valor = ' ))

    if escolha == 1:
        soma = n1 + n2
        print('A soma entre os numeros {} e {} e igual a {}'.format(n1, n2, soma))
    elif escolha ==2:
        multi = n1 * n2
        print('A multiplicao entre {} e {} e igual a {}'.format(n1, n2, multi))
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior numero entre {} e {} e igual a {}'.format(n1, n2, maior))
    elif escolha == 4:
        print ('Informe os numeros novamente!')
        n1 = int(input('Primeiro valor ='))
        n2 = int(input('Segundo valor ='))
    else:
        print('Finalizando....')
    print('-=' * 20)
    sleep(2)
    print('fim do programa!')