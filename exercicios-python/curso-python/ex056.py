soma = 0
quant = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    quant = quant + 1
    soma = soma + num
print(f'Você digitou {quant} números e a soma entre eles foi {soma}.')
