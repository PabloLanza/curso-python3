from time import sleep
print('-------Supermercado-------')
total = 0
prod1000 = 0
nomebarato = ''
menorpreco = 0
cont = 0
while True:
    produto = str(input('Digite o nome do produto: ')).title()
    preco = float(input('Digite o preço do produto: '))
    print('-------' * 4)
    total = total + preco
    cont = cont + 1
    if preco > 1000:
        prod1000 = prod1000 + 1
    if cont == 1:
        menorpreco = preco
        nomebarato = produto
    if preco < menorpreco:
        menorpreco = preco
        nomebarato = produto
    op = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    print('-------' * 4)
    if op not in 'S':
        break
print('Processando....')
sleep(1)
print(f'''Total gasto na compra foi R${total:.2f}
{prod1000} produtos custam mais de R$1000.00
O produto mais barato foi o(a) {nomebarato} custando R${menorpreco:.2f}''')
print('PROGRAMA ENCERRADO')
