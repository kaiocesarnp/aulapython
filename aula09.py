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

