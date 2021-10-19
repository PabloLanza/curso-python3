def leia_Int(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m ERRO! Digite um valor inteiro! \033[m')
        if ok:
            break
    return valor



n = leia_Int('Digite um valor inteiro: ') 
print(f'\033[0;32m Você digitou o número {n} \033[m')