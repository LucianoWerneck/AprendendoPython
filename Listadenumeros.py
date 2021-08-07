num = list()
while True:
    n = int(input('Digite um Número: '))
    if n not in num:
        num.append(n)
        print('Numero adicionado.')
    else:
        print('Numero já existente.')
    resp = str(input('Quer Continuar: [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
num.sort()
print('-='*22)
print(f'Os números digitados foram: {num}')
