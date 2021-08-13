'''Media e presença do Aluno'''
nome = str(input('Nome do aluno: '))
nota1 = float(input('Nota 1ª Prova: '))
nota2 = float(input('Nota 2ª Prova: '))
faltas = int(input('Quantas Faltas: '))
media = (nota1 + nota2) / 2
presença = ((faltas*100/30)*-1+100)
if media >= 6 and presença >= 70:
    print(f'O aluno {nome} foi aprovado com {media} media com {"%.0f" % presença}% de presença.')
elif media <= 6 and presença < 70:
    print(f'Aluno {nome} foi reprovado por meida baixa e excesso de faltas.')
elif media < 6:
    print('Reprovado por Media Baixa.')
elif presença < 70:
    print('Reprovado por Excesso de Faltas.')