termo = int(input('Informe o primeiro termo = '))
razao = int(input('informe a razao = '))
decimo = termo + (10 -1) * razao
for c in range(termo, decimo + razao, razao):
    print(c)