alt = int(input('Qual a altura da parede? '))
larg = int(input('Qual a largura da parede? '))
area = alt * larg
tinta = area / 2
print('A área dessa parede é {} metros quadrados e você precisará de {} litros de tinta para pintá-la!' .format(area, tinta))
