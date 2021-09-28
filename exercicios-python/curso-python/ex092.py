def fatorial(num, show=False):
    f = 1
    if show == True:
        for c in range(num, 0, -1):
            f *= c
            print(f'{c} x', end=' ')
        print(f'= {f}')
    elif show == False:
        for c in range(num, 0, -1):
            f *= c
        return f
            


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n, True)}')