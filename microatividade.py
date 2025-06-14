#Microatividade 1: Descrever como ler um arquivo
#CSV usando a biblioteca Pandas (Python)

import pandas as pd

# Leitura do arquivo CSV com separador ";"
df = pd.read_csv('picoweb.csv', sep=';', engine='python', encoding='utf-8')

# Exibição dos dados 

#print(df)        #Tire o "#" para Usar o Codigo


#Microatividade 2: Descrever como criar um
#subconjunto de dados a partir de um conjunto
#existente usando a biblioteca Pandas (Python)

# Criar subconjunto com 3 colunas 

#sub_df = df[['Date', 'Pulse', 'Calories']]        #Tire o "#" para Usar o Codigo

# Exibição do subconjunto 
#print(sub_df)                 #Tire o "#" para Usar o Codigo


#Microatividade 3: Descrever como configurar o
#número máximo de linhas a serem exibidas na
#visualização de um conjunto de dados usando a
#biblioteca Pandas (Python)

# Configurar para exibir até 9999 linhas
pd.set_option('display.max_rows', 9999)

# Exibir todas as linhas do DataFrame
#print(df.to_string())    #Tire o "#" para Usar o Codigo

#Microatividade 4: Descrever como exibir as
#primeiras e últimas “N” linhas de um conjunto de
#dados usando a biblioteca Pandas (Python)

#print("Imprimir as primeiras 10 linhas")   #Tire o "#" para Usar o Codigo

# Exibir primeiras 10 linhas
#print(df.head(10))     #Tire o "#" para Usar o Codigo

#print("Imprimir as últimas 10 linhas")  #Tire o "#" para Usar o Codigo

# Exibir últimas 10 linhas
#print(df.tail(10))    #Tire o "#" para Usar o Codigo


#Microatividade 5: Descrever como exibir
#informações gerais sobre as colunas, linhas e dados
#de um conjunto de dados usando a biblioteca
#Pandas (Python)

print("Informações Gerais Sobre o Conjunto de Dados: ")
# Exibir informações gerais sobre o DataFrame
df.info()
