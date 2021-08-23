import pandas as pd

'''df = pd.read_csv("ocorrencia_2010_2020.csv", sep=";", parse_dates=['ocorrencia_dia'], dayfirst=True)
df.head()
df.loc[1, 'ocorrencia_cidade']
'BELÉM'
pd.set_option('display.max_columns', 10)
print(df.loc[1:3])
df.codigo_ocorrencia.is_unique
df.set_index('codigo_ocorrencia', implace=True)'''
print(df.loc[[10,40]])
