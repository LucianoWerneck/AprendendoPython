'''Validando a Extração de Dados e aprendendo dataframe'''
import pandas as pd
import pandera as pa

df = pd.read_csv("ocorrencia_2010_2020.csv", sep=";", parse_dates=["ocorrencia_dia"], dayfirst=True)
del df["codigo_ocorrencia1"]
df = df.drop(df.columns[[ 2, 3, 5, 6, 9, 13, 14, 15, 16, 17, 19, 20]], axis=1)
pd.set_option('display.max_columns', 10)
print(df.tail(10))
print(df.info)
print(df.dtypes)
#print(df.ocorrencia_dia.dt.month)
schema = pa.DataFrameSchema(
    columns = {
        "codigo_ocorrencia":pa.Column(pa.Int, required=False),
        "codigo_ocorrencia2":pa.Column(pa.Int),
        "ocorrencia_classifcacao":pa.Column(pa.String),
        "ocorrencia_cidade":pa.Column(pa.String),
        "ocorrencia_uf":pa.Column(pa.String, pa.Check.str_length(2,2)),
        "ocorrencia_aerodromo":pa.Column(pa.String),
        "ocorrencia_dia":pa.Column(pa.DateTime),
        "ocorrencia_hora":pa.Column(pa.String, pa.Check.str_matches
        (r'^([0-1]?[0-9]│[2][0-3]):([0-5][0-9])(:[0-5][0-9])?$'), nullable=True),
        "total_recomendacoes":pa.Column(pa.Int)
    }
)


