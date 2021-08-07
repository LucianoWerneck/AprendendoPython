'''Criando Lista de Números separando os Pares dos Impares'''
list =[[],[]]
valor = 0
quant = int(input('Quantos números você quer digitar: '))
for c in range(1,quant):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        list[0].append(valor)
    else:
        list[1].append(valor)
print('-='*20)
list[0].sort()
list[1].sort()
print(f'Lista valores pares: {list[0]}')
print(f'Lista valores impares: {list[1]}')