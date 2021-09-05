viag = float(input('Quantos km têm a viagem? '))
viacurta = float(viag * 0.50)
vialonga = float(viag * 0.45)
if viag <= 200:
    print('O preço da passagem será de R${:.2f}.'.format(viacurta))
else:
    print('O preço da passagem será de R${:.2f}'.format(vialonga))
