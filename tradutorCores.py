resp = 'S'
cores = {'preto': 'black', 'verde': 'green', 'vermelho': 'red', 'branco': 'white',
         'rosa': 'pink', 'roxa': 'purple', 'marron': 'brown', 'cinza': 'gray',
         'prata': 'silver', 'dourada': 'golden', 'amarelo': 'yellow', 'azul': 'blue'}
while True:
    cor = input('Escolha a cor que deseja traduzir:\n').lower()
    tradução = cores.get(cor, 'Esta cor não consta no meu dicionario')
    print(tradução)
    print('-'* 25)
    resp = str(input('Deseja continuar(S/N): ').upper())
    print('-'*25)
    if resp == 'N':
        break
