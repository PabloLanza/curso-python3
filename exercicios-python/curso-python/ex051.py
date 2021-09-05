idadecont = 0
contmulher = 0
maioridadehomem = 0
nomevelho = ''
for c in range (1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).lower().strip()
    idadecont += idade
    if c == 1 and sexo in 'm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'f' and idade < 20:
        contmulher += 1
mediaidade = idadecont / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e seu nome é {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(contmulher))
    