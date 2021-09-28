from random import randint
from time import sleep
lista = list()


def sorteio():
    for c in range(0, 5):
        lista.append(randint(1, 100))
    print(f'Os números sortedos foram {lista}')


def soma_par():
    soma = 0
    print(f'Os números pares sorteados foram: ', end='')
    for n in lista:
        if n % 2 == 0:
            soma = soma + n
            print(n, end=' ')
    print()
    print(f'A soma dos números pares sorteados foi {soma}')


sorteio()
sleep(1)
soma_par()