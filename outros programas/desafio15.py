q = float(input("Quantos km o carro andou ? "))
d = float(input("De quantos dias foi o aluguel do carro? "))
s = (q * 0.15)+(d * 60)
print("O valor total a ser pago é de {}".format(s))