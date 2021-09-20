cont = 0
param = 10
while True:
    cont = 0
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    while cont < 10:
        cont = cont + 1
        tab = num * cont
        print(f'{num} x {cont} = {tab}')
print('PROGRAMA ENCERRADO')

