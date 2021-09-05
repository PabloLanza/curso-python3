termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão dessa PA: '))
decimo = termo + (10 - 1)  * razao
for c in range(termo, decimo + 1, razao):
    print(c, end='-')
