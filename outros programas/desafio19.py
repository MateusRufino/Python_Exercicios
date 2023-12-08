import random
a = str(input("Digite o nome do aluno 1 = "))
b = str(input("Digite o nome do aluno 2 = "))
c = str(input("Digite o nome do aluno 3 = "))
d = str(input("Digite o nome do aluno 4 = "))
lista = (a, b, c, d)
escolhido = random.choice(lista)
print("O nome escolhido é {}".format(escolhido))
