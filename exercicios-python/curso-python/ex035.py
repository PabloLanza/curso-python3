nome = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
media = (n1 + n2)/2
if media < 5.0:
    print('O aluno {} foi reprovado com média {}.'.format(nome, media))
elif media >= 7:
    print('O aluno {} foi aprovado com média {}.'.format(nome, media))
else:
    print('O aluno {} teve média {} e irá fazer recuperação.'.format(nome, media))
