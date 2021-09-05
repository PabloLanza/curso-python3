from datetime import date
print('Olá, vamos te informar sobre o alistamento militar 2021.')
nasc = int(input('Digite em qual ano você nasceu: '))
ano = date.today().year
ida = ano - nasc
if ida < 18:
    alist = 18 - ida
    print('Você deverá se aistar em {} ano(s).'.format(alist))
elif ida > 18:
    alist = ida - 18
    print('Você já deveria ter se alistado a {} ano(s). Compareça a junta de serviço militar mais próxima para regularizar a sua situação.'.format(alist))
else:
    print('Atenção! Está na hora de se alistar.')
