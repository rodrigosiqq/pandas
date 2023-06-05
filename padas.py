import pandas as pd


df = pd.read_excel('vendas.xlsx')


print(df.head())


print(df.info())


print(df.describe())


print(df['Categoria'].value_counts())
