import math
catopo = int(input('Qual o comprimento do cateto oposto? '))
catadj = int(input('Qual o comprimento do cateto adjacente? '))
hip = math.hypot(catopo, catadj)
print('A hipotenusa é {}' .format(hip))