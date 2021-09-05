from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Bem Vindo ao Jokempo no Python.
Suas Opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual a sua jogada? '))
print('Jo')
sleep(1)
print('Kem')
sleep(1)
print('Po')
sleep(1)
print('=-' * 11)
print('Jogador jogou {}'.format(itens[jogador]))
print('Computador jogou {}'.format(itens[computador]))
print('=-' * 11)
if computador == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador Venceu!')
    elif jogador == 2:
        print('Computador Venceu!')
    else:
        print('Opção Inválida!')
elif computador == 1:
    if jogador == 0:
        print('Computador Venceu!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador Venceu!')
    else:
        print('Opção Inválida!')
elif computador == 2:
    if jogador == 0:
        print('Jogador Venceu!')
    elif jogador == 1:
        print('Computador Venceu!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Opção Inválida!')

