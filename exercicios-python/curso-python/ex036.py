from datetime import date
nasc = int(input('Digite o ano em que o atleta nasceu: '))
ano = date.today().year
ida = ano - nasc 
if ida <= 9:
    print('O atleta está na categoria Mirim.')
elif ida <= 14:
    print('O atleta está na cetegoria Infaltil.')
elif ida <= 19:
    print('O atleta está na categoria Júnior.')
elif ida == 20:
    print('O atleta está na categoria Sênior.')
else:
    print('O atleta está na categoria Master.')
