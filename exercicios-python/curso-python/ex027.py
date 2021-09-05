n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n1 < n2 < n3:
    print('O menor número é: {} e o maior é {}'.format(n1, n3))
if n1 < n3 < n2:
    print('O menor número é: {} e o maior é {}'.format(n1, n2))
if n2 < n1 < n3:
    print('O menor número é {} e o maior é {}'.format(n2, n3))
if n2 < n3 < n1:
    print('O menor número é {} e o maior é {}'.format(n2, n1))
if n3 < n1 < n2:
    print('O menor número é {} e o maior é {}'.format(n3, n2))
if n3 < n2 < n1:
    print('O menor número é {} e o maior é {}'.format(n3, n1))