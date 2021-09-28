from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} até {f} pulando de {p} em {p}:')
    if p == 0:
        p = 1
    if i > f:
        if p < 0:
            for c in range(i, f, p):
                print(c, end=' ', flush=True)
                sleep(0.7)
            print()
            print('-' * 30)
        else:
            for c in range(i, f, -p):
                print(c, end=' ', flush=True)
                sleep(0.7)
            print()
            print('-' * 30)
    else:
        for c in range(i, f, p):
            print(c, end=' ', flush=True)
            sleep(0.7)
        print()
        print('-' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('De: ')), int(input('Até: ')), int(input('De quanto em quanto: ')))