def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar o valor!\033[m')
            return 0
        else:
            return n


def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar o valor!\033[m')
            return 0
        else:
            return n



numi = leia_int('Digite um valor inteiro: ')
numf = leia_float('Digite um valor real: ')
print(f'O valor inteiro digitado foi {numi} e o valor real digitado foi {numf}')