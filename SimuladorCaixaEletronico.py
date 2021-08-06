print('='*35)
print('{:^35}'.format('_-- LuBank --_'))
print('='*35)
saque = int(input('Qual valor do Saque? R$ '))
total = saque
contnota = 0
nota = 50
while True:
    if total >= nota:
        total -= nota
        contnota += 1
    else:
        if contnota > 0:
            print(f'Total de {contnota} cedulas de R${nota} .')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        contnota = 0
        if total == 0:
            break

