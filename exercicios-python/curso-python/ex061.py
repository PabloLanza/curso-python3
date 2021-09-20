from time import sleep
print('-------Banco do Brasil-------')
while True:
    valor = int(input('Digite o valor do saque: '))
    ced50 = valor // 50
    ced20 = (valor % 50) // 20
    ced10 = ((valor % 50) % 20) // 10
    ced1 = (((valor % 50) % 20) % 10) // 1
    break
print('PROCESSANDO SAQUE...')
sleep(1)
print('CONTANDO NOTAS...')
sleep(1)
print('----' * 7)
print(f'''Saque processado
Notas de R$50: {ced50}
Notas de R$20 :{ced20}
Notas de R$10: {ced10}
Notas de R$1: {ced1}''')