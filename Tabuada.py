'''Programa para Criar Tabuada'''
while True:
    n = int(input('Digite um Número para saber sua Tabuada:  '))
    if n <= 0:
        break
    print('_'*12)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('_'*12)
    print('Digite 0 para Encerrar.')
