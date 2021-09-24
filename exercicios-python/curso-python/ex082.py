from datetime import date
cadastro = {}
cadastro["nome"] = str(input('Nome: '))
ano = int(input('Nascimento: '))
cadastro["nascimento"] = ano
cadastro["idade"] = date.today().year - ano
cart = int(input('Carteira de Trabalho (0 não possui): '))
if cart != 0:
    cadastro["ctps"] = cart
    contratação = int(input('Ano de contratação: '))
    cadastro["contratação"] = contratação
    cadastro["salário"] = float(input('Salário: '))
    cadastro["aposentadoria"] = contratação + 35
for i, v in cadastro.items():
    print(f'{i} tem o valor {v}')