# PANDAS

# O que é pandas?
# Uma biblioteca de código aberto para prover estruturas de dados de alto nível e
    # ferramentas para análise de dados fáceis de usar, com alto desempenho, para a linguagem Python

# Documentação da biblioteca pandas:
# https://pandas.pydata.org/pandas-docs/stable/index.html
# Guia do usuário (Pandas em 10 minutos):
# https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html

# Como usar pandas?
# pandas faz uso de duas estruturas de dados principais:
#  Series e Dataframe
# A biblioteca pandas foi construída sobre numpy…

# ----------
# A estrutura de dados Series
# Uma série é simplesmente um array de 1 dimensão, mas…
    # Contém o array de dados: qualquer tipo de dado suportado pelo NumPy
    # Contém também um array de rótulos associados (labels), chamados de índices

# ----------------
# Exemplo da estrutura de dados Series

# import pandas as pd

# lista = [-5, 0, 8, -12, 100, 33, 7, -1, 1, 2]
# serie = pd.Series(lista) #constroi uma variavel a partir desta lista, atribuida a variavel 'serie'
# type(serie)
        #class 'pandas.core.series.Series'   = esse é o 'type(serie)', o tipo que ela representa
# print(serie)
    # ao dar o print, a coluna da esquerda mostra os indices(1,2,3,4...)
        # e do lado direito são os valores, o conjunto de dados

# Indexação de Series
# Se o índice não for especificado, o padrão consiste de inteiros
    # indo de 0 até N-1 (onde N é o comprimento dos dados)...

# ----------------------



