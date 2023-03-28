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








