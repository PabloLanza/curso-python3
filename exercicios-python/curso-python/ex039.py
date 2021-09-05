preco = float(input('Qual o preço do produto? '))
condicao = int(input('Qual a forma de pagamento?\n 1 - Cartão\n 2 - Dinheiro/Cheque\n'))
if condicao == 1:
    forma = int(input('1 - A Vista\n 2 - Parcelado\n'))
    if forma == 1:
        precoatual = float(preco - preco * 0.05)
        print('Você ganhou 5 por cento de desconto. O preço ficará R${:.2f}.'.format(precoatual))
    elif forma == 2:
        parc = int(input('Você deseja parcelar em:\n 1 - 2 vezes\n 2 - 3 ou mais vezes\n'))
        if parc == 1:
            print('O produto continua no valor de R${:.2f}.'.format(preco))
        elif parc ==2:
            precoatual = float(preco + preco * 0.20)
            print('O produto agora custará R${:.2f}.'.format(precoatual))
        else:
            print('Opção Inválida! Tente Novamente.')
    else:
        print('Opção Inválida! Tente Novamente.')
elif condicao == 2:
    precoatual = float(preco - preco * 0.10)
    print('Você ganhou 10 por cento de desconto. O produto agora custará R${:.2f}.'.format(precoatual))
else:
    print('Opção Inválida! Tente Novamente.')


