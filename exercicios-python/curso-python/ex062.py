numero = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    num = int(input('Digite um número: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {numero[num]}.')
        break
    else:
        print('Número inválido. Tente novamente!')