def area(l, c):
    arte = l * c
    print(f'O Terreno tem {l} Largura {c} de comprimento.'
          f'\n A área é de {arte}m².')


print('-' * 15)
print('Controle de Terrenos')
print('-' * 15)
larg = float(input('Qual a Largura do Terreno: '))
comp = float(input('Qual o Comprimento do Terreno: '))
area(larg, comp)