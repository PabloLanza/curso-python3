s = 0
cont = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        s += num
        cont += 1
print('Você informou {} número(s) PARES e a soma entre eles é {}'.format(cont, s))

