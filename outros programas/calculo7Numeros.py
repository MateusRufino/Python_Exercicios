soma = 0
cont = 0
for c in range(1, 7, ):
    num =int(input('Digite o {} numeoro: '.format(c)))
    if num % 2 ==0:
        soma = soma + num
        cont = cont + 1

print("A soma {} numeros pares informados e igual a  {}".format(cont, soma))

