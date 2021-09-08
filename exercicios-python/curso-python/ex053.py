primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Você gostria de mostrar nais quantos termos?: '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
print('FIM')