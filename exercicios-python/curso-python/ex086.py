def area(l, c):
    result = l * c
    print(f'A área do terreno {l} x {c} é {result}')


print('-' * 30)
print(' << CALCULANDO ÁREA >>')
print('-' * 30)
area(float(input('Digite a largura do terreno: ')), float(input('Digite o comprimento do terreno: ')))
