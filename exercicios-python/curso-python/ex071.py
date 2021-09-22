val = list()
c = 0
while True:
    val.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? S/N: ')).strip().upper()[0]
    if resp in 'N':
        break
print(f'Você digitou {len(val)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(val, reverse=True)}')
if 5 in val:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')