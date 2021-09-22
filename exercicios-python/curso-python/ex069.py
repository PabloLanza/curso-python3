val = list()
while True:
    num = int(input('Digite um número: '))
    if num in val:
        print('Valor ja consta na lista.')
    else:
        val.append(num)
        print('Valor adicionado com sucesso...')
    resp = str(input('Quer continuar? S/N: ')).strip().upper()[0]
    if resp in 'N':
        break
print(f'Você digitou {sorted(val)}')