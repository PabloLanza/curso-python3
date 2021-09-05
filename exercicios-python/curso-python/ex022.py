import random
numcomp = random.randint(0, 5)
numusu = int(input('O computador escolheu um número de 0 à 5, tente advinhar qual foi! Número: '))
if numusu == numcomp:
    print('O computador escolheu {}. Parabéns! Você acertou!'.format(numcomp))
else:
    print('O computador escolheu {}. Infelizmente você errou!'.format(numcomp))
print('Fim do programa!')