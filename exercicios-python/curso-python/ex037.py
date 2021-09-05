r1 = float(input('Digite o comprimrnto da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo com essas retas.')
    if r1 == r2 == r3:
        print('O triângulo formado será EQUILÁTERO.')
    elif r1 == r2 or r1 == r3 or r3 == r2:
        print('O triângulo formado será ISÓSCELES.')
    else:
        print('O triângulo formado será ESCALENO.')
else:
    print('Não é possível formar um triângulo com essas retas.')
