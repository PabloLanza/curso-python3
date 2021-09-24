
aprov = dict()
partidas = list()
geral = list()
while True:
    aprov["nome"] = str(input('Qual o nome do jogador: '))
    quant = int(input(f'Quantas partidas {aprov["nome"]} jogou:: '))
    soma = 0
    for c in range(0, quant):
        gols = int(input(f'Quantos gols na partida {c}: '))
        soma = soma + gols
        partidas.append(gols)
    aprov["gols"] = partidas.copy()
    partidas.clear()
    aprov["total"] = soma
    geral.append(aprov.copy())
    aprov.clear()
    resp = str(input('Quer continuar? S/N: ')).strip().upper()[0]
    if resp in 'N':
        break
print(f'{"Cod":<4}{"Nome":<10}{"Gols":^20}{"Total":^7}')
print('-' * 42)
for d, a in enumerate(geral):
    print(f'{a:<4}{d["nome"]:<10}{d["gols"]:^20}{d["total"]:^7}')
print('-' * 42)

