import pandas as pd
import numpy as np

# Etapa 1: Leitura do CSV
df = pd.read_csv('picoweb.csv', sep=';', engine='python',encoding='utf-8')

# Etapa 2: Exibir informações
print(df.info())
print(df.head())
print(df.tail())

# Etapa 3: Criar cópia do DataFrame
df_limpo = df.copy()

# Etapa 4: Substituir valores nulos de 'Calories' por 0
df_limpo['Calories'].fillna(0, inplace=True)
print(df_limpo)

# Etapa 5: Substituir valores nulos de 'Date' por '1900/01/01'
df_limpo['Date'].fillna('1900/01/01', inplace=True)
print(df_limpo)

# Etapa 6: Tentar converter para datetime (irá falhar por causa do "1900/01/01" e "20201226")
try:
    df_limpo['Date'] = pd.to_datetime(df_limpo['Date'], format='%Y/%m/%d')
except Exception as e:
    print("Erro ao converter datas:", e)

# Etapa 7: Corrigir a data "1900/01/01" substituindo por NaN
df_limpo['Date'].replace('1900/01/01', np.nan, inplace=True)

# Corrigir valor específico "20201226" para "2020/12/26"
df_limpo['Date'].replace('20201226', '2020/12/26', inplace=True)

# Nova tentativa de conversão
df_limpo['Date'] = pd.to_datetime(df_limpo['Date'], errors='coerce')
print(df_limpo)

# Etapa 8: Remover registros com valores nulos (como a linha com Date NaN)
df_limpo.dropna(subset=['Date'], inplace=True)

# Exibir o DataFrame final limpo
print(df_limpo)
