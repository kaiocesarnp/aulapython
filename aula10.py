# VISUALIZAÇÃO DE DADOS

# Visualização com matplotlib
# Referências para estudo:
# ▸ https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
# ▸ https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html

# A biblioteca “tradicional” para confeccionar gráficos é a MatPlotLib.
# Pandas faz uso da MatPlotLib de maneira fácil.
# Para usar os plots do MatPlotLib, além de importar o Pandas no seu programa, faça:
# import pandas as pd
# import matplotlib.pyplot as plt

# Visualização de DataFrames com matplotlib
# Relembrando o DataFrame de pessoas:

import pandas as pd
import matplotlib.pyplot as plt

dados = {'nome': ["Ana", "Bob", "Cleo"],
 'idade': [50, 36, 2],
 'altura': [1.5, 1.73, .61]}
df = pd.DataFrame(dados, columns = ['nome', 'idade', 'altura'])

# Gerando gráficos:
#                                             # o 'plot' gera um objeto gráfico em memória
# df.plot(x='idade', y='altura', kind='bar') #'kind = 'bar'' = tipo de gráfico = barra
# plt.show() #'plt' vem da importação de matplotlib e 'show' é para mostrar o gráfico

# Organizar o eixo 'x' de forma ascendente, do menor para o maior:

sdf = df.sort_values('idade') #cria-se um novo dataframe, que é uma versão do original com os valores ordeados (sort_values) na coluna 'idade'
sdf.plot(x='idade', y='altura', kind='bar')
plt.show()

# ---------------------
# OUTROS TIPOS DE GRÁFICOS

# Top 5 (five):

#       MUNICÍPIO       CASOS       ÓBITOS POR COVID-19
# 20    Curitiba        245996          8163
# 305   Londrina        144141          2397
# 262   Maringá         115613          1735
# 44    Ponta Grossa    80137           1471
# 143   Cascavel        75249           1207

# forma mais simples:
# top5.plot(kind='bar') 'top5' = nome do dataframe, 'kind=bar' = tipo de gráfico, barra
# plt.show()

# ------
# rotular o eixo x de acordo com a coluna “MUNICÍPIOS”:
# top5.plot(kind='barh', x='MUNICÍPIO', y=['CASOS', 'ÓBITOS POR COVID-19'])
# plt.show()
            # barh = barra horizontal



