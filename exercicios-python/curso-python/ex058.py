import random
while True:
    print('----Ímpar ou Par----')
    comp = random.randint(0,10)
    op = int(input('''Escolha:
    1 - Ímpar
    2 - Par
    Sua opção: '''))
    usu = int(input('Agora escolha um número: '))
    result = usu + comp
    if op == 1 and result % 2 == 0 or op == 2 and result % 2 != 0: 
        print(f'''O computador jogou {comp}
        Você jogou {usu}
        Resultado: {result}
        VOCÊ PERDEU!''')
        break
    else: 
        print(f'''O computador jogou {comp}
        Você jogou {usu}
        Resultado: {result}
        VOCÊ GANHOU!!''')
print('PROGRAMA ENCERRADO')


