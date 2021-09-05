sal = float(input('Digite o seu salário: '))
aum1 = float(sal + sal * 0.10)
aum2 = float(sal + sal * 0.15)
if sal > 1250.00:
    print('Seu novo salário será R${}.'.format(aum1))
else:
    print('Seu novo salário será R${}.'.format(aum2))


