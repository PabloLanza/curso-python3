lista = list()
dic = dict()

while True:
    dic["nome"] = str(input('Nome: '))
    dic["idade"] = int(input('Idade: '))
    dic["sexo"] = str(input('Sexo [F/M]: ')).strip().upper()[0]
    lista.append(dic.copy())
    dic.clear()
    resp = str(input('Quer continuar? S/N: ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(lista)
print('-=' * 30)
print(f'Foram cadastradas {len(lista)} pessoas.')
soma = 0
for d in lista:
    soma = soma + d["idade"]
media = soma/len(lista)
print(f'A média de idade do grupo é {media:.1f} anos.')
print(f'As mulheres cadastradas foram: ', end='')
for d in lista:
    if d["sexo"] in 'F':
        print(f'{d["nome"]}', end=' ') 
print()
print(f'As pessoas com idade acima da média são ', end='')
for d in lista:
    if d["idade"] > media:
        print(f'{d["nome"]} com {d["idade"]} anos.', end=' ')
print()
print('-=' * 30)
print('<<< PROGRAMA ENCERRADO >>>')