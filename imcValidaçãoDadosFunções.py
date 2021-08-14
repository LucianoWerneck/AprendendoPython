def imc(peso, altura) :
    imc = peso / (altura * altura)
    return imc

def class_imc(sexo, peso, altura) :
    valor_imc = imc(peso, altura)

    if sexo == 'm':
        if valor_imc < 20.7:
            return "Abaixo do peso"
        elif valor_imc >= 20.7 and valor_imc < 26.4:
            return "Peso normal"
        elif valor_imc >= 26.4 and valor_imc < 30.0:
            return "Sobrepeso"
        elif valor_imc >= 30.1 and valor_imc < 34.9:
            return "Obesidade grau I"
        elif valor_imc >= 35.0 and valor_imc < 39.9:
            return "Obesidade grau II"
        elif valor_imc >= 40.0:
            return "Obesidade Mórbida"
        else:
            return "Erro de cálculo. Entre em contato com nossa administração"
    if sexo == 'f':
        if valor_imc < 19.1:
            return "Abaixo do peso"
        elif valor_imc >= 19.1 and valor_imc < 25.8:
            return "Peso normal"
        elif valor_imc >= 25.8 and valor_imc < 27.3:
            return "Sobrepeso"
        elif valor_imc >= 27.3 and valor_imc < 32.3:
            return "Obesidade grau I"
        elif valor_imc >= 32.3 and valor_imc < 36.5:
            return "Obesidade grau II"
        elif valor_imc >= 36.5:
            return "Obesidade Mórbida"
        else:
            return "Erro de cálculo. Entre em contato com nossa administração"

print('Vamos calcula o seu imc ?')

valid_sexo = False
while valid_sexo == False:
    sexo = input('Digite o seu sexo (M ou F): ').lower()
    if sexo != 'm' and sexo != 'f':
        print('Sexo inválido. Digite M ou F.')
    else:
        valid_sexo = True
        print('\n')

valid_peso = False
while valid_peso == False:
    peso = input('Digite o peso. (Ex: 62.5): ')
    try:
        peso = float(peso)
        if peso <= 0 or peso > 300:
            print('Peso inválido. Número não pode ser zero nem negativo.')
        else:
            valid_peso = True
            print('\n')
    except:
        print('Peso inválido. Use apenas números e separe os decimais com ponto.')

valid_altura = False
while valid_altura == False:
    altura = input('Digite a altura em metros.(Ex: 1.70): ')
    try:
        altura = float(altura)
        if altura <= 0 or altura >= 2.5:
            print('Altura inválida. Digite um número superior a zero.')
        else:
            valid_altura = True
            print('\n')
    except:
        print('Altura inálida. Use apenas números e separe decimais com ponto.')

v_imc = imc(peso, altura)
c_imc = class_imc(sexo, peso, altura)
print(f'Seu IMC é : {"%.2f" % v_imc} a classificação é : {c_imc} ')
