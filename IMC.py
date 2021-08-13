def imc(peso, altura) :
    imc = peso / (altura * altura)
    return imc

def class_imc(sexo, peso, altura) :
    valor_imc = imc(peso, altura)
    if sexo == 'm':
        if imc < 20.7:
            return "Abaixo do peso"
        elif i