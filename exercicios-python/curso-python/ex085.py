aprov = {}
partidas = list()
time = list()
while True:
    aprov.clear()
    aprov["nome"] = str(input('Qual o nome do jogador: '))
    quant = int(input(f'Quantas partidas {aprov["nome"]} jogou: '))
    partidas.clear()
    for c in range(0, quant):
        partidas.append(int(input(f'Quantos gols na partida {c}: '))) 
    aprov["gols"] = partidas[:]
    aprov["total"] = sum(partidas)
    time.append(aprov.copy())
    while True:
        resp = str(input('Deseja continuar? S/N: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in aprov.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)
while True:
    busca = int(input('Qual o código do jogador? (999 interrompe): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' ---- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} ----')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'     No jogo {i+1} fez {g} gols.')
        print('-' * 40)
print('<< VOLTE SEMPRE >>')
