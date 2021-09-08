resp = 'S'
soma = media = quant = maior = menor = 0
while resp in 'S':
    num = int(input('Digite um número: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else: 
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print('''Menor número digitado: {}
Maior número digitado: {}
Quantidade de números digitados: {}
Média entre os números digitados: {}'''.format(menor, maior, quant, media))
