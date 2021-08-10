'''Função que faz contagem crescente de
 0 a 10 e decresente 10 a 0 com passo de 2
 e uma ultima contagem personalizada'''

from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='* 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    print('-='* 20)
    sleep(0.3)

    if i < f:
        cont = 0
        while cont <= f:

            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont += p
        print('FIM')
    else :
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= p
        print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)
print('-='* 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Final: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)