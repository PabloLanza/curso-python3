from datetime import date
contmaior = 0
contmenor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?: '.format(c)))
    atual = date.today().year
    idade = atual - nasc
    if idade >= 21:
        contmaior = contmaior + 1
    else:
        contmenor = contmenor + 1
print('{} pessoas são maiores de idade e {} ainda são menores'.format(contmaior, contmenor))
    