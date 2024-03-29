# PANDAS PARTE 1

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
#  serie.values  = para ver os valores
# type(serie.values)  = tipo dos valores
# serie.index = para ver os indices, RangeIndex(start=0, stop=10, step=1) = do 0 ao 9, pulado de 1 em 1
# type(serie.index)  = tipo de indices        RangeIndex = indice de intervalo

# -------------------
# Criação de uma Série
# Os dados de uma série podem ser várias coisas, por exemplo:
# 1. Uma lista = (lista = [10, 11, 12])
# 2. Um ndarray (array n-dimensional NumPy) = (ndata = np.random.randn(3)) = gera um vetor ndimensional numpy aleatorio com tres numeros aleatorios obedecendo uma distribuição normal/padrao centrada em 0 
# 3. Um escalar = pd.Series(3) 
# 4. Uma tupla = (dtup = (11, 22))
# 5. Um dicionário Python = (dict = {‘a’: 1, ‘b’: 2})

# ------------------
# Indexação “personalizada” de Series
# O método básico para ser criar uma série é:
# S = pd.Series(dados, index=indice) 
# S = variavel que recebe a serie
# pd.Series = construtor 
# dados: objetos como citado nos slides anteriores
# index: uma lista de rótulos para o eixo.          Opcional, pois se passar só os dados, ja é tranformada numa série 

# Exemplo:

# import pandas as pd
# serie2 = pd.Series([4, 7, 1], index=['d', 'g', 'a'])
# print(serie2)
# type(serie2)

    # lista de valores inteiros, e o index representa o indice de cada valor inteiro, ou seja, d=4, g=7

# ---------------
# dicionario

# import pandas as pd
# dict2 = {'a': 0, 'b': 1, 'c': 2}
# serie2 = pd.Series(dict2) 
# print(serie2)
# type(serie2)

# ------------
# dicionario com novos indices:

# import pandas as pd
# dict2 = {'a': 0, 'b': 1, 'c': 2}
# serie2 = pd.Series(dict2, index=["b", "c", "d", "a"])   # o 'd' vira NaN, que é um ponto flutuante
# print(serie2)
# type(serie2)

# ----------------------
# Acesso a elementos de Series
# A forma para se acessar um valor de uma série indexada é igual a outros objetos:
# import pandas as pd
# serie1 = pd.Series([10, 11, 12])
# print(serie1)
# type(serie1)

#----------------
# Operações sobre Series

# SOMAR todos os elementos:
    # serie.sum() 

# Encontrar o VALOR MÁXIMO:
    #serie.max( )

# Encontrar o VALOR MÍNIMO:
    #serie.min( )

# serie.median()  Mediana
    # 1.5

#serie.mean()   Média
    # 13.3

# Documentação:
# https://pandas.pydata.org/docs/reference/api/pandas.Series.html

# ---------------------
# O Método describe()
# serie.describe()
# O método describe gera estatísticas descritivas!
# Resume tendências centrais, dispersão e formato de uma distribuição de dados, excluíndo valores NaN.
    # Permite analisar dados numéricos e objetos:
    # Para dados numéricos, inclui:
    # Contagem, média, descio padrão, valores mínimo e máximo, e percentis

# Para dados de objetos, o resultado inclui:
    #Contagem, únicos, top (mais comum) e frequência (valor do elemento top)

# l = ['a', 'a', 'b', 'c', 'd', 'a', 'c']
    #s = pd.Series(l)

# s.describe()
# count 7           7 valores
# unique 4          4 são unicos
# top a             o A é que aparece mais vezes 
# freq 3            a frequencia do top é 3
# dtype: object 

# --------------------
# EXERCÍCIOS
# Questão 01
# Suponha os códigos a seguir. Associe cada um deles com a saída correta esperada.
# ATENÇÃO: Pode haver mais de um código com a mesma saída!

# import pandas as pd

# lis1 = [1, 2]
# ser1 = pd.Series(lis1, index =["b", "a"])
# print(ser1.values)

# -------
# import pandas as pd

# lis1 = [1, 2]
# ser1 = pd.Series(lis1)
# print(ser1.index)

# -------
# import pandas as pd

# dic1 = {"a":1, "b":2}
# ser1 = pd.Series(dic1)
# print(ser1.index)

# -------
# import pandas as pd

# lis1 = [1, 2]
# ser1 = pd.Series(lis1, index =["b", "a"])
# print(ser1.index)

# -------
# import pandas as pd

# lis1 = [1, 2]
# ser1 = pd.Series(lis1, index =["a", "b"])
# print(ser1.values)

# ---------------------------
# Questão 02

# Considere o código abaixo. Baseado na execução do programa e o arquivo "stairwaytoheaven.txt" 
    # servindo como parâmetro para o primeiro argumento de entrada, assinale a alternativa correta.

# import sys
# import pandas as pd

# arquivo = open(sys.argv[1]).read()
# arquivo = open("c:/users/particular/desktop/stairwaytoheaven.txt").read()


# text = [palavra.strip("\n") for palavra in arquivo.split()]
# s1 = pd.Series(text)

# print(s1.describe())


#  i. Há 348 palavras na lista atribuída à variável "text".
# ii. Do total de palavras, se desconsiderarmos as palavras repetidas, temos 174 palavras distintas.
# iii. A palavra que aparece mais vezes é "heaven", com frequência igual a 15.
# iv. O método describe() não funciona com séries baseadas em strings.

# Escolha uma ou mais:
# a. Todas as assertivas são FALSAS.
# b. Somente a assertiva iv é FALSA.
# c. Somente as assertivas ii e iv são FALSAS.
# d. Somente a assertiva i é VERDADEIRA.                    RESPOSTA
# e. Somente as assertivas i e iii são VERDADEIRAS.

# ---------------