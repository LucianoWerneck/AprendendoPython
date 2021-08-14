'''Media e presença do Aluno Com Validação'''
nome = str(input('Nome do aluno: '))

valid_nota = False
while valid_nota == False:
    nota1 = input('Digite a Nota da 1ª Prova: ')
    try:
        nota1 = float(nota1)
        if nota1 < 0 or nota1 > 10:
            print('Nota inválida. Valor deve ser entre 0 e 10.')
        else:
            valid_nota = True
    except:
        print('Nota inválida. Use apenas números e separe os decimais com ponto. (Ex. 9.5).')
valid_nota = False
while valid_nota == False:
    nota2 = input('Digite a Nota da 2ª Prova: ')
    try:
        nota2 = float(nota2)
        if nota2 < 0 or nota2 > 10:
            print('Nota inválida. Valor deve ser entre 0 e 10.')
        else:
            valid_nota = True
    except:
        print('Nota inválida. Use apenas números e separe os decimais com pornto. (Ex. 9.5).')

valid_faltas = False
while valid_faltas == False:
    faltas = input('Quantas Faltas o aluno teve: ')
    try:
        faltas = float(faltas)
        if faltas < 0 or faltas > 30:
            print('Número de faltas inválido. Valor de ser entre 0 e 30.')
        else:
            valid_faltas = True
    except:
        print('Número de faltas inválido. Use apenas números e separe os decimais com ponto.')

media = (nota1 + nota2) / 2
presença = ((30 - faltas)/30)*100
if media >= 6 and presença >= 70:
    print(f'O aluno {nome} foi aprovado com media {media} e com {"%.0f" % presença}% de presença.')
elif media <= 6 and presença < 70:
    print(f'Aluno {nome} foi reprovado por meida baixa e excesso de faltas.')
elif media < 6:
    print('Reprovado por Media Baixa.')
elif presença < 70:
    print('Reprovado por Excesso de Faltas.')
