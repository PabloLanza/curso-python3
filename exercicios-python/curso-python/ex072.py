val = list()
par = list()
impar = list()
while True:
    num = int(input('Digite um número: '))
    val.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    resp = str(input('Deseje cpntinuar? S/N: ')).strip().upper()[0]
    if resp in 'N':
        break
print(f'Lista Completa: {sorted(val)}')
print(f'Lista Par: {sorted(par)}')
print(f'Lista Ímpar: {sorted(impar)}')
