def ficha(nome='', gols=''):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} tem {gols} gols no campeonato.')



nome = str(input('Digite o nome do jogador: '))
gols = str(input('Quantos gols ele tem no campeonato: '))
ficha(nome, gols)