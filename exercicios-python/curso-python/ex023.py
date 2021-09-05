vel = int(input('Qual a velocidade do carro? '))
x = vel - 80
multa = float(7.00 * x)
if vel > 80:
    print('Ih. Você foi multado no valor de R${:.2f}, pois passou a {}km/h em uma via de 80km/h'.format(multa, vel))
else:
    print('Você estava dentro da velocidade permitida nessa via!')
