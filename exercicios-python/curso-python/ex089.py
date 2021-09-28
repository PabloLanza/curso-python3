from time import sleep


def maior(* lst):
    print('-=' * 30)
    print('ANALISANDO OS VALORES PASSADOS...')
    print(f'{lst} -- Foram informados {len(lst)} valores ao todo.')
    print(f'O maior valor informado foi {max(lst)}.')
    print('-=' * 30)
    sleep(0.5)


maior(1, 2, 3, 4, 5, 6, 7)
maior(70, 45, 20, 65)
maior(1000, 144, 12, 170, 2)
maior(7, 5, 25)