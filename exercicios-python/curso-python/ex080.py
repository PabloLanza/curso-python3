aluno = {}
aluno["Nome"] = str(input('Nome: '))
aluno["Média"] = float(input('Média: '))
if aluno["Média"] >= 6:
    aluno["Situação"] = 'Aprovado'
else:
    aluno["Situação"] = 'Reprovado(a)'
for i, a in aluno.items():
    print(f'{i}: {a}')