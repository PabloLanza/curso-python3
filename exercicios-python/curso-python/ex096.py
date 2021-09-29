c = ('\033[m',
'\033[0;30;41m',
'\033[0;30;42m',
'\033[0;30;43m',
'\033[0;30;44m',
'\033[0;30;45m',
'\033[7;30m');


def ajuda(com):
    linha(f'Acessando o manual do comando \'{op}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')


def linha(txt, cor=0):
    tam = len(txt) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'{txt}')
    print('~' * tam)
    print(c[0], end='')


while True:
    linha('SISTEMA DE AJUDA PyHELP', 2)
    op = str(input('Função ou Biblioteca > ')).strip()
    if op.upper() == 'FIM':
        break
    else:
        ajuda(op)
    linha('Acessando o manual do comando')
    help(op)
linha('Volte Sempre', 1)