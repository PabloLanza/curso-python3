from random import randint
from time import sleep
jog = {}
c = 1
mai = men = 0
for c in range(1, 5):
    jog[f"Jogador{c}"] = randint(1, 6)
for j, d in jog.items():
    print(f'O dado do {j} caiu em {d}')
    sleep(1)
print('---- RANKING DE JOGADORES ----')
for j, d in jog.items():
    if j == "Jogador1":
        mai = d
        men = d
    if d > mai:
        mai = d
    if d < men:
        men = d

