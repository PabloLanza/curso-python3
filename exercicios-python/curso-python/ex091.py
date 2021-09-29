def voto(num=0):
    from datetime import date
    idade = date.today().year - num
    if idade >= 18:
        if idade > 65:
            return 'OPCIONAL'
        else:
            return 'OBRIGATÓRIO'
    elif idade < 18:
        return 'NÃO VOTA'
    


nasc = int(input('Digite o seu ano de nascimento: '))
print(f'VOTO: {voto(nasc)}')