preco = float(input('Digite o preço normal o produto = '))
print('Formas de pagamento \n 1 = À vista no dinheiro / cheque \n 2 = À vista no cartão \n 3 = em até 2 vezes no cartão \n 4 = 3 vezes ou mais no cartão')
forma = int(input('Digite o numero da forma de pagamento = '))

if forma == 1:
    print('O preco com 10% de desconto ficara {}'.format(preco * 0.9))

elif forma == 2:
    print('O preco com 5% de desconto ficara {}'.format(preco * 0.95))

elif forma == 3:
    print('O preco ficara {}'.format(preco))

elif forma == 4:
    print('O preco com o aumento de 20% ficara {}'.format(preco * 1.2))

else:
    print('Opcao inexistente, digite uma opcao valida')