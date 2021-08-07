from uteis import dados as t
cont = SuperFizzBuzz = FizzBuzz = Fizz = Buzz = SFZ = 0
t.titulo('SuperFizzBuzz')
n = t.leiaInt('Digite Quantos Numeros Deseja Analisar: ')
lista = []
while n != SuperFizzBuzz:
    cont += 1
    if cont % n == 0 :
        n = SuperFizzBuzz
        SFZ += 1
        print(f'{cont} SuperFizzBuzz')
    if cont % 3 == 0 and cont % 5 == 0:
         FizzBuzz += 1
         print(f'{cont} FizzBuzz')
    elif cont % 3 == 0:
        Fizz += 1
        print(f'{cont} Fizz')
    elif cont % 5 == 0:
        Buzz += 1
        print(f'{cont} Buzz')
    else:
        lista.append(cont)

while True:
    resp = str(input('Quer ver os numeros neutros [S/N]: ')).lower()
    if resp != 'n' and resp != 's':
        print('Resposta Incorreta use [S/N].')
    elif resp == 's':
        print(lista)
        break
    else:
        break

print('-_-'* 15)
print(f'\033[31mForam analisados \033[m{cont}\033[31m elementos.\033[m')
print(f'\033[32mIndice:\033[m\nSuperFizzBuzz:{SFZ}\nFizzBuzz:{FizzBuzz}\nFizz:{Fizz}\nBuzz:{Buzz}.')