from time import sleep
def maior(* num):
    cont = maior = 0
    print('Analisando os Valores Passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
maior(2, 9, 4, 5, 7, 11)
