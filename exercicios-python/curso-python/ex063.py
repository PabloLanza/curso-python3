brasileirao = ('','Atlético MG', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians', 'Internacional', 'Fluminense', 'Athlético PR', 'Cuiabá', 'Atlético GO', 'São Paulo', 'Ceará', 'Santos', 'Bahia', 'Juventude', 'Grêmio', 'América MG', 'Sport', 'Chapecoense')
print('=-=-=-=' * 10)
print(f'Classificação: {brasileirao[1:21]}')
print('=-=-=-=' * 10)
print(f'Os 5 primeiros são: {brasileirao[1:6]}')
print('=-=-=-=' * 10)
print(f'Os 4 últimos são: {brasileirao[-4:]}')
print('=-=-=-=' * 10)
print(f'Em ordem alfabética: {sorted(brasileirao[1:21])}')
print('=-=-=-=' * 10)
print(f'A Chapecoense está na {brasileirao.index("Chapecoense")}ª posição')