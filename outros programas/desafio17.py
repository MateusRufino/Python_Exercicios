import math
cato = float(input("Digite o cateto oposto = "))
cata = float(input("Digite o cateto adjascente = "))
res = math.hypot(cato, cata)
print("O comprimento da hipotenusa é {:.2f} ".format(res))