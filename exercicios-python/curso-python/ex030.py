nome = str(input('Qual é o seu nome? '))
if nome == 'Pablo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Ana':
    print('Seu nome é bem comum no Brasil!')
elif nome in 'Jéssica Cláudia Júlia':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha uma ótimo dia {}!'.format(nome))