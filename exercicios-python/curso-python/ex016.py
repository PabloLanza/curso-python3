nome = str(input('Qual o seu nome completo? ')).strip()

print('Analisando o seu nome......')
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome possui {} caracteres'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro é {} e possui {} letras'.format(separa[0], len(separa[0])))
