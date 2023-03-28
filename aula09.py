# PANDAS PARTE 2

# Objetivos da aula
# Apresentar a biblioteca pandas e suas funcionalidades
# Analisar dados compostos por múltiplos tipos

# Referências adicionais
# Introdução a Estruturas de Dados: https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html
# Documentação da biblioteca pandas: https://pandas.pydata.org/pandas-docs/stable/index.html
# Guia do usuário (Pandas em 10 minutos): https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html

# Como usar pandas?
#pandas faz uso de duas estruturas de dados principais:
    #Series (vista na aula passada) e  Dataframe

# DataFrame
# É uma estrutura de dados:
    #Rotulada, ou seja, tem nomes para seus eixos, sejam colunas ou linhas
    #De 2 (duas) dimensões
    #Com colunas de tipos potencialmente diferentes, por exemplo
        # primeira coluna nomes, segunda datas, terceira pontos flutuantes

# A estrutura de dados DataFrame pode ser “enxergada” como:
    #Uma planilha (parecida com Excel)
    #Uma tabela SQL
    #Um dicionário de objetos do tipo Series

# Exemplo de DataFrame

# NOME IDADE ALTURA
# Ana   50    1.50
# Bob   36    1.73
# Cleo  2     0.61

# Entradas
# Assim como as Series, um DataFrame aceita diversos tipos de entradas:
    #Dicionário de 1D ndarrays, listas, dicionários, séries.
    #ndarrays (NumPy) de duas dimensões (2-D numpy.ndarray)
    #ndarray estruturado
    #Uma série (Series)
    #Outro DataFrame

# Juntamente com os dados, pode-se passar:
#Rótulos de linha (índices)
#Rótulos de coluna (colunas)
            # Isto causa o descarte de índices e valores específicos de um dicionário de Series!!!

# import pandas as pd

# dados = {                               #3 chaves: nome, idade, altura. cada uma com seus valores
# 'nome': ["Ana", "Bob", "Cleo"], 
# 'idade': [50, 36, 2],
# 'altura': [1.5, 1.73, .61]
# }                                       

# print(pd.Series(dados)) 

# ---------------

# Como criar um DataFrame?

# Forma errada:   
        # Quando se imprime o dataframe criado a partir de uma série, os indices já foram obtidos
        # a partir das chaves do dicionário, e como os valores são litas, assume-se que via
        # 'serie1', há apenas uma coluna (a coluna zero [0]), composta de 3 listas
# import pandas as pd

# dados = {
# 'nome': ["Ana", "Bob",
# "Cleo"],
# 'idade': [50, 36, 2],
# 'altura': [1.5, 1.73, .61]
# }

# serie1 = pd.Series(dados)
# df1 = pd.DataFrame(serie1)
# print(df1)

# --------------
# Forma certa:
                # 3 colunas, sendo as chaves do dicionario. Uma coluna só com nomes, outra só com
                # idades, outra só com altura.
# import pandas as pd

# dados = {
# 'nome': ["Ana", "Bob",
# "Cleo"],
# 'idade': [50, 36, 2],
# 'altura': [1.5, 1.73, .61]
# }

# df1 = pd.DataFrame( dados)
# print(df1)

# -----------------------------------------------
# DataFrame - Entradas (* CUIDADO!)

import pandas as pd

dados = {
'nome': ["Ana", "Bob",
"Cleo"],
'idade': [50, 36, 2],
'altura': [1.5, 1.73, .61]
}

serie1 = pd.Series(dados)
df1 = pd.DataFrame(serie1, index=['a', 'nome', 'c'])   #dois parametros passados na construção do dataframe
print(df1)                                          #serie1 e index que recebe uma lista de indices
                                                    #que não estão na lista original então nada será
                                                    # impresso na saída, só NaN. Uma coluna só [0]


# DataFrame - Entradas de dict
# O índice resultante é a união dos índices… Exemplo:
# dados = {
#  "TRE-1": pd.Series([1, 0, 5], index=["1/jan/2022", "31/jan/2022", "2/fev/2022"]),
#  "TRE-2": pd.Series([3, 10], index=["1/jan/2022", "1/fev/2022"]),
#  "TRE-3": pd.Series([0, 2, 1, 4], index=["31/jan/2022", "2/fev/2022", "10/fev/2022", "31/mar/2022"])
#  }

# df = pd.DataFrame(dados)

# RESULTADO:
#             TRE-1   TRE-2   TRE-3
# 1/fev/2022  NaN     10.0    NaN
# 1/jan/2022  1.0     3.0     NaN
# 10/fev/2022 NaN     NaN     1.0
# 2/fev/2022  5.0     NaN     2.0
# 31/jan/2022 0.0     NaN     0.0
# 31/mar/2022 NaN     NaN     4.0      
    # Ordem alfabética das string, 1 vem antes do 10, que vem antes do 31
# Se nenhum parâmetro é passado para o argumento “columns”, 
    # elas serão a lista de chaves do dicionário…

# --------------
# O índice passado pode sobrepor os existentes, causando seleção de dados… Exemplo:
# dados = {
#  "TRE-1": pd.Series([1, 0, 5], index=["1/jan/2022", "31/jan/2022", "2/fev/2022"]),
#  "TRE-2": pd.Series([3, 10], index=["1/jan/2022", "1/fev/2022"]),
#  "TRE-3": pd.Series([0, 2, 1, 4], index=["31/jan/2022", "2/fev/2022", "10/fev/2022", "31/mar/2022"])
#  }

# df = pd.DataFrame(dados, index=["1/jan/2022", "1/fev/2022", "1/mar/2022"])

#             TRE-1 TRE-2     TRE-3
# 1/jan/2022  1.0     3.0     NaN
# 1/fev/2022  NaN     10.0    NaN
# 1/mar/2022  NaN     NaN     NaN
    # O índice “1/mar/2022” não está associado a nenhum dado…

# ----------------
# DataFrame - Entradas de dict
# As colunas também “selecionam” os dados… Exemplo:

# dados = {
#  "TRE-1": pd.Series([1, 0, 5], index=["1/jan/2022", "31/jan/2022", "2/fev/2022"]),
#  "TRE-2": pd.Series([3, 10], index=["1/jan/2022", "1/fev/2022"]),
#  "TRE-3": pd.Series([0, 2, 1, 4], index=["31/jan/2022", "2/fev/2022", "10/fev/2022", "31/mar/2022"])
#  }
# df = pd.DataFrame(dados, index=["1/jan/2022", "1/fev/2022", "1/mar/2022"], columns=["TRE-2", "TRE-4"])

#             TRE-2   TRE-4
# 1/jan/2022  3.0     NaN
# 1/fev/2022  10.0    NaN
# 1/mar/2022  NaN     NaN

# A chave “TRE-4” não está presente no dicionário de entrada (“dados”)

# ----------------------------------

# Métodos
# Acesso às dimensões

# print(df.index) = mostra os indices do dataframe
# print(df.columns) = mostra as colunas do dataframe

# ---------
# método describe()

import pandas as pd
dados = {
'nome': ["Ana", "Bob", "Cleo"],
'idade': [50, 36, 2],
'altura': [1.5, 1.73, .61]
}

df1 = pd.DataFrame(dados)
# print(df1)
# print(df1.describe())

# Qual a maior idade encontrada no data frame?
maxidade = df1['idade'].max()
# ● Quem é mais baixo?
minaltura = df1['altura'].min()
# ● Qual a média de altura?
mediaaltura = df1['altura'].mean()
# Qual a soma das idades?
somaidades = df1['idade'].sum()

print(maxidade)
print(minaltura)
print(mediaaltura)
print(somaidades)

# ---------------------------
# Operações

# ▸ Inserção de novas colunas
# ▸ Remoção de colunas
# ▸ Concatenação de dados
# ▸ Remoção de duplicatas
# ▸ Ajuste de índices
# ▸ Identificação de dados faltantes
# ▸ Preenchimento de dados faltantes

# -------------
# Inserção:
# NOVA LISTA DE VALORES:
#  Pesos = [50.8, 75, 11.3]
# INSERÇÃO DA COLUNA
#  df['peso'] = Pesos

# ------
# Remoção:
#   nome  idade altura peso
# 0 Ana    50    1.50    1
# 1 Bob    36    1.73    2
# 2 Cleo   2     0.61    3

# del df['nome']

# -------
# Remoção 2:

#       idade   altura    peso
# 0     50      1.50    1
# 1     36      1.73    2
# 2     2       0.61    3

# df.pop['peso']

# ----------
# Concatenação de novos dados
# df2 = pd.DataFrame([[50, 1.50]],
#  columns=['idade', 'altura'])

#       idade altura
# 0     50      1

# -------------
# Concatenar Dataframes
# df3 = pd.concat([df, df2])

# df
#       idade   altura
# 0     50      1.50
# 1     36      1.73
# 2     2       0.61

# df2
#       idade   altura
# 0     50      1.50

# Resultado df3:
#       idade   altura
# 0     50      1.50
# 1     36      1.73
# 2     2       0.61
# 0     50      1.50    Nova linha inserida!

# ------------------------------
# Duplicatas e Índices
# df3 = pd.concat([df, df2])
#  df3
#       idade   altura
# 0     50      1.50
# 1     36      1.73
# 2     2       0.61
# 0     50      1.50        A primeira e a última linha são iguais

# se fizer um 'df3.drop(0)' remove todos os indices zero [0] do dataframe
    # O “drop()”, quando recebe apenas um argumento, atua sobre o índice.
        # Logo, “drop(0)” remove todos os índices com esse valor…

# SOULÇÃO:
# df3.drop_duplicates() = conserva o primeiro valor e remove os outros iguais a ele
    # O “drop_duplicates()” atua sobre os dados.
        # Logo, sua execução irá ignorar os índices e considerar os valores das colunas…

# ------------
# Ajuste de índices 1
# Para evitar o problema da remoção de índices duplicados:
    # Utilize 'pd.concat([df, df2], ignore_index=True)'
        # Os índices são refeitos com uma nova sequência

# Resultado:
#       idade   altura
# 0     50      1.50
# 1     36      1.73
# 2     2       0.61
# 3     50      1.50

# ----------
# Ajuste de índices 2
# Para evitar o problema da remoção de índices duplicados:
#df3 = pd.concat([df, df2])
#df3.reset_index()
    # Cria novos indices, mas mantem os orignais numa nova coluna, cujo o nome é 'index' 

# Resultado:

#    index idade  altura
# 0   0     50     1.50
# 1   1     36     1.73
# 2   2     2      0.61
# 3   0     50     1.50

# ---------
# Já a utilização de 'df3.reset_index(drop=True)' remove os indices originais

#       idade   altura
# 0     50      1.50
# 1     36      1.73
# 2     2       0.61
# 3     50      1.50

# ------------
# Para evitar reatribuição:
# df3.reset_index(drop=True, inplace=True)

# ------------
# Dados faltantes (identificação)
# Suponha o seguinte DataFrame:
# df
#   nome    idade altura peso
# 0 Ana     50      1.50 1
# 1 Bob     36      1.73 2
# 2 Cleo    2       0.61 3


# Suponha outro Dataframe:
# # df2
#   idade   altura
# 0 50       1.50

# Ao concatenarmos ambos, temos:
# >>> df3 = pd.concat([df, df2], ignore_index=True)
#   nome    idade altura    peso
# 0 Ana     50      1.50    51.0
# 1 Bob     36      1.73    75.0
# 2 Cleo    2       0.61    7.0
# 3 NaN     50      1.50    NaN


# Para identificar dados faltatens utiliza-se 'df3.isna()'
#   nome    idade   altura    peso
# 0 False   False   False     False
# 1 False   False   False     False
# 2 False   False   False     False
# 3 True    False   False     True

# ------------
# Descartar os dados faltantes
# df3.dropna()

#   nome    idade altura    peso
# 0 Ana     50      1.50    51.0
# 1 Bob     36      1.73    75.0
# 2 Cleo    2       0.61    7.0
# 3 NaN     50      1.50    NaN   -> Esta linha é descartada ao utlizar o comando

# -----------
# Preenchê-los de outra forma
#  df3.fillna(-1)

#   nome    idade altura    peso
# 0 Ana     50      1.50    51.0
# 1 Bob     36      1.73    75.0
# 2 Cleo    2       0.61    7.0
# 3 -1      50      1.50    -1.0

# ----------
# Preenchê-los de outra forma
# df3.fillna("N/D")

#   nome    idade   altura  peso
# 0 Ana     50      1.50    51.0
# 1 Bob     36      1.73    75.0
# 2 Cleo    2       0.61    7.0
# 3 N/D     50      1.50    N/D

# --------------------
# Carga de arquivos CSV
# O carregamento de um arquivo CSV no Pandas é muito fácil:
# import pandas as pd
# arquivo = pd.read_csv('processados.csv', names=['data', 'atendimentos'])
# print(arquivo)

#           data      atendimentos
# 0       2018-01-08      20722
# 1       2018-06-18      12008
# 2       2021-11-13      39402
# 3       2018-10-03      20094
# 4       2022-02-05      840
# .. ... ...
# 995     2022-02-11      18455
# 996     2021-09-04      13438
# 997     2019-10-18      39686
# 998     2018-07-20      48460
# 999     2020-04-26      4356
# [1000 rows x 2 columns]

# ---------------
# Agrupamento e contagem
# Quantas vezes cada data aparece no DataFrame?
# arquivo.groupby("data").count()

# data  
# 2018-01-02    3      vezes que cada data aparece
# 2018-01-03    1
# 2018-01-05    1
# 2018-01-07    1
# 2018-01-08    3
# ... ...
# 2022-03-11    1
# 2022-03-14    3
# 2022-03-17    1
# 2022-03-21    2
# 2022-03-22    2

# -------------
# Qual o acumulado de atendimentos por data?
# arquivo.groupby("data").sum()

# ----------
# Ao observarmos a primeira coluna do DataFrame anterior,
    # temos um dado que parece uma data (ano-mês-dia).
# Vamos verificar?
#  type(df['data'][0])   acesso ao arquivo 'df', coluna 'data', indice '[0]'
# class 'str'>    
        # = o valor é uma string, para o sistema

# Tranformando em data de fato:
# Para facilitar comparações, temos que transformar a primeira
# coluna em um tipo "data"...
# import pandas as pd
# import sys
# import datetime

# arquivo = pd.read_csv(sys.argv[1], names=['data', 'atendimentos'])
# arquivo['data'] = pd.to_datetime(arquivo['data'])  = converte a coluna data para data de fato

# print(type(arquivo['data'][0]))
        # = <class 'pandas._libs.tslibs.timestamps.Timestamp'>

# -----------------
# arquivo['data'].describe()
# count 1000    total linhas
# unique 734    734 das linhas são unicas
# top 2019-11-26 00:00:00   data que mais aparece
# freq 5                frequencia com que ela aparece
# first 2018-01-02 00:00:00     data minima 
# last 2022-03-22 00:00:00      data maxima
# Name: data, dtype: object     

# --------
# Lidando com datas
# Podemos precisar comparar datas no nosso DataFrame.
# Por exemplo:
# Quais dados tem data antes de certa data?
    # df['data'][df['data'] < datetime.datetime(2018, 1, 1)]
        # quais elementos da coluna df data que tem uma data menor que 1/1/2018
# Retorno:
# Series([], Name: data, dtype: datetime64[ns])
    # vazia, pois não ha nada antes da data mencionada

# Quais dados possuem uma data específica?
# ▸ df['data'][df['data'] == datetime.datetime(2018, 12, 10)]
# Retorno:
# 260 2018-12-10
# 492 2018-12-10
# 596 2018-12-10
# 617 2018-12-10
# Name: data, dtype: datetime64[ns]

# Quantos atendimentos foram feitos por ano?
#  df.groupby(df['data'].dt.to_period('Y'))['atendimentos'].sum()
        # dt = metodo que permite o acesso a uma estrutura de dados dentro do dataframe 
            # to_period = por periodo / (y) = year/ ano, mas pode ser mes, dia da semana...
# data
# 2018 6116615
# 2019 6772594
# 2020 5985430
# 2021 5130308
# 2022 1147776
# Freq: A-DEC, Name: atendimentos, dtype: int64












