aprov = {}
partidas = list()
aprov["nome"] = str(input('Qual o nome do jogador: '))
quant = int(input(f'Quantas partidas {aprov["nome"]} jogou:: '))
soma = 0
for c in range(0, quant):
    partidas.append(int(input(f'Quantos gols na partida {c}: '))) 
aprov["gols"] = partidas[:]
aprov["total"] = sum(partidas)
print('-=' * 30)
print(aprov)
print('-=' * 30)
for c, v in aprov.items():
    print(f'O campo {c} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {aprov["nome"]} jogou {len(aprov["gols"])} partidas.')
for c, g in enumerate(aprov["gols"]):
    print(f'Na partida {c}, fez {g} gols.')
print('-=' * 30)
