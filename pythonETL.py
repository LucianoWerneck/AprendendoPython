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
        "codigo_ocorrencia":pa.Column(pa.Int)
    }
)


