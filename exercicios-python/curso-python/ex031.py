print('Olá, precisamos de algumas informações!')
valorcasa = float(input('Qual o valor da casa? '))
anos = int(input('Em quantos anos você irá pagar a casa? '))
sal = float(input('Qual o seu salário mensal? '))
valorpres = (valorcasa / anos)/12
print('O valor da prestação mensal é R${:.2f}.'.format(valorpres))
if valorpres > (sal * 0.30):
    print('Empréstimo Negado! Infelizmente você não poderá realizar este empréstimo, pois o valor da prestação mensal é superior a 30 por cento de seu salário')
else:
    print('Empréstimo Liberado!')
