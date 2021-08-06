''' Leitor de Valores que retorna o maior e menor e suas respequitivas posições'''

valores = list()
maior = menor = 0
quant = int(input('Quantos números vc quer Digitar: '))

for num in range(0, quant):
    valores.append(int(input(f'Digite um valor para a Posição {num}: ')))
    if num == 0:
        maior = menor = valores[num]
    else:
        if valores[num] > maior:
            maior = valores[num]
        if valores[num] < menor:
            menor = valores[num]
print('=_'* 20)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}.', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}.', end='')
