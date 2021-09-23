matriz = list()
linha1 = list()
linha2 = list()
linha3 = list()
for c in range(0, 3):
    linha1.append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0, 3):
    linha2.append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0, 3):
    linha3.append(int(input(f'Digite um valor para [2, {c}]: ')))
matriz.append(linha1[:])
matriz.append(linha2[:])
matriz.append(linha3[:])
linha1.clear()
linha2.clear()
linha3.clear()
print(f'{matriz[0][0]} {matriz[0][1]} {matriz[0][2]}')
print(f'{matriz[1][0]} {matriz[1][1]} {matriz[1][2]}')
print(f'{matriz[2][0]} {matriz[2][1]} {matriz[2][2]}')
