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

# import pandas as pd
# import matplotlib.pyplot as plt

# dados = {'nome': ["Ana", "Bob", "Cleo"],
#  'idade': [50, 36, 2],
#  'altura': [1.5, 1.73, .61]}
# df = pd.DataFrame(dados, columns = ['nome', 'idade', 'altura'])

# Gerando gráficos:
#                                             # o 'plot' gera um objeto gráfico em memória
# df.plot(x='idade', y='altura', kind='bar') #'kind = 'bar'' = tipo de gráfico = barra
# plt.show() #'plt' vem da importação de matplotlib e 'show' é para mostrar o gráfico

# Organizar o eixo 'x' de forma ascendente, do menor para o maior:

# sdf = df.sort_values('idade') #cria-se um novo dataframe, que é uma versão do original com os valores ordeados (sort_values) na coluna 'idade'
# sdf.plot(x='idade', y='altura', kind='bar')
# plt.show()

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

# ------
# E se quisermos ver as barras acumuladas?
# ax = top5.plot(kind='bar', x='MUNICÍPIO', y='CASOS')
#     # variavel 'ax' recebe o daraframe 'top5', criado com 'plot', tipo barra e recebe municipios e casos

# top5.plot(kind='bar',
#     x='MUNICÍPIO',
#     y='ÓBITOS POR COVID-19',  # eixo y agora é obitos
#     ax=ax,   # usa-se como eixo de pilotagem o primero 'ax', mencionado no começo
#     color='red') # cor das barras
# plt.show()

# -------
# Com eixo y rotulado:
# plt.ylabel("Quantidade")

# -------
# Com rótulos do eixo x rotacionados 45 graus:
# plt.xticks(rotation=45)    = pontos marcados no eixo x

# -------
# Em escala logarítmica:
# plt.yscale("log")

# ---------------------------
# Gráfico de Pizza:

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("c:/users/particular/desktop/obitoscasos.csv", 
#                  delimiter=";", usecols=['municipio', 'data último óbito', 'dias após último óbito'])
#     # cria-se um dataframe 'df', pd.read_csv lê o csv, delimitador é ponto e virgula, e usa as colunas municipios, casos e obitos
# df.sort_values(by=['data último óbito'], inplace=True, ascending=False)
#     # 'sort_values' ordena os valores, 'by' = por casos, 'inplace=true' tira a necessidade de fazer uma ordenação, 'asceding=false' vai do menor para o maior
# top5 = df.head(5) # Obtém os 5 maiores valores

# #kind=pie = pizza/torta
# top5.plot(kind='pie', y='data último óbito', labels=top5['municipio'], autopct='%1.1f%%')
#             # labels = rotulos, autopct='%1.1f%% = aceita dados em ponto flutuante, tem uma casa após o float e o porcento na frente
# plt.show()

# -------------------------
# Médias Móveis
# Uma média móvel usa “janelas deslizantes” para mostrar a média de um período de tempo, 
    # evitando conclusõesimprecisas devido a picos e vales sazonais.
    #Permite melhor visualização das tendências dos dados
    #“Achata” as flutuações que dificultam a interpretação

# Com a média móvel e janela de 7 dias
# Trecho de Código:

# ax=dfcovid['Novos'].plot(label="Novos Casos") 'ax' = variavel, dfcovid = dataframe, 'novos' = coluna usada, plot(label) rotulado como 'novos casos'. Como não foi passado nada, será linha ao inves de barras, pizza..
# ax.set_ylabel("Casos") = nome ao lado, y = alturua
# ax.set_title("COVID-19 no PR")   #título do gráfico

# mediamovel = dfcovid.Novos.rolling(7).mean() = nova estrutura de dados chamada 'mediamovel', baseada no df do covid, na coluna novos, usando o metodo 'rolling' com a janela deslizante pulando de 7 em 7 pontos, e tire a media(mean)
# mediamovel.plot(label='Média Móvel', color='orange')

# ----------
# Para outros tipos de rolling, basta substituir mean() pelo
    # método que se deseja, por exemplo, std().
# Tipos de rolling possíveis:
# https://pandas.pydata.org/docs/reference/window.html

# ------------------------------
# SEABORN
# Ferramenta para visualização de dados baseada em Matplotlib.
# Interface de (ainda mais) alto nível que o Matplotlib para geração de gráficos.

# Algumas funções:
# relplot
# relplot é uma função flexível para gerar gráficos mostrando as relações entre variáveis.
# Por padrão, os gráficos gerados são de dispersão (scatter)
# Veja a documentação em:
# seaborn.pydata.org/generated/seaborn.relplot.html

# import seaborn as sns
# sns.relplot(data=dados, x=nomeX, y=nomeY)

# dados: conjunto de dados (e.g., dataframe Pandas)
# x = nome da coluna que possui o eixo X
# y = nome da coluna que possui o eixo Y

# -------------
# Exemplo:
# Considere o arquivo ExemploNotas2.csv
#       Nome;  Prova1;  Prova2;     Período;    Escola
# Aluno   0;    100;    100;        Manhã;      Escola 1
# Aluno   1;    93;     92;         Manhã;      Escola 1
# Aluno   2;    93;     100;        Manhã;      Escola 1
# Aluno   6;    100;    95;         Manhã;      Escola 1

# Vamos exibir em um gráfico de dispersão a relação entre a 
    # nota na primeira com a segunda prova para os alunos.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

notas_df = pd.read_csv("c:/users/particular/desktop/ExemploNotas2.csv",delimiter=';')
sns.relplot(data=notas_df)
# sns.relplot(data=notas_df, x="Prova1", y="Prova2")
# sns.set_theme()
# sns.set_theme(palette="icefire")
plt.show()


# O Seaborn possui vários temas padrão para estilizar o gráfico
# Use a função sns.set_theme() [mencionado no código acima]
# Você pode chamar a função sem parâmetros (vai aplicar o estilo padrão), 
    # ou modificar paletas, fontes, estilos, …
# Veja a documentação aqui
# seaborn.pydata.org/generated/seaborn.set_theme.html

# ----------------
# Adicionando informações
# Vamos mudar a cor e o formato de cada ponto de acordo com o período que o aluno estuda
# sns.relplot(..., hue=cor, style=estilo)
# cor: coluna no datraframe que controla a cor
# estilo = coluna no datraframe que controla o estilo

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# notas_df = pd.read_csv("c:/users/particular/desktop/ExemploNotas2.csv",delimiter=';')
# sns.set_theme(palette="icefire")
# sns.relplot(data=notas_df, x="Prova1", y="Prova2", hue="Período", style="Período")
# plt.show()

# ----------------



