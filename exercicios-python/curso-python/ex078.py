from random import randint
megasena = list()
palpites = list()
c = 0
quant = int(input('Quantos jogos você quer gerar? '))
for c in range(0,quant):
    for c in range(0, 6):
        palpites.append(randint(1, 60))
    megasena.append(palpites[:])
    palpites.clear()
print(megasena)