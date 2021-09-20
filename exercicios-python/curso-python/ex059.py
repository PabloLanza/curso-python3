print('Cadastro de Pessoas')
conthomens = 0 
contmaior = 0
contmulher20 = 0
while True:
    sexo = str(input('Digite o sexo da pessoa: ')).upper().strip()[0]
    idade = int(input('Digite a idade da pessoa: '))
    if sexo in 'M':
        conthomens = conthomens + 1
    if idade >= 18:
        contmaior = contmaior + 1
    if sexo in 'F' and idade < 20:
        contmulher20 = contmulher20 + 1
    op = str(input('Deseja contiuar? [S/N]:' )).upper().strip()[0]
    print('=-=-' * 20)
    if op not in 'S':
        break
print(f'''Temos {contmaior} pessoas maiores de 18 anos.
Foram cadastrados {conthomens} homens.
Temos um total de {contmulher20} mulheres com menos de 20 anos.''')
print('PROGRAMA ENCERRADO')

