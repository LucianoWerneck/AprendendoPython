''' Somando Números '''

n = s = 0
while True:
    n = int(input('Digite um Número : '))
    if n == 999:
        break
    s += n
    print('Digite 999 para encerrar e somar.')
print(f'A soma dos Números digitados é {s}')