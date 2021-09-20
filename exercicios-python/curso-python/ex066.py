listagem = ('Lapis', 1.20, 'Caneta', 1.50, 'Borracha', 2.50, 'Caderno', 15.00, 'Mochila', 70.00, 'Livro', 20.10)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')