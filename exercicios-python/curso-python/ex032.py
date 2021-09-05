import math
print('Olá! Bem Vindo ao sistema de conversão numérica.')
num = int(input('Digite o número que você deseja fazer a conversão: '))
op = int(input('Você quer converter o número {} para:\n 1 - Binário\n 2 - Octal\n 3 - Hexadecimal\n'.format(num)))
if op == 1:
    print('O número {} em Binário é: {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('O número {} em Octal é: {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('O númer {} em Hexadecimal é: {}'.format(num, hex(num)[2:]))
else: 
    print('Opção Inválida! Tente novamente.')
