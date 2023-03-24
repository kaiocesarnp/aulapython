# NumPy - Operações Lógicas

# Where
# A função numpy.where(condition, resultado_if, resultado_else) retorna um array com 
    #os elementos que satisfazem determinada condição
# condition é a condição
# resultado_if são os elementos selecionados quando a condição é satisfeita
# Resultado_else são os elementos selecionados quando a condição não é satisfeita

# import numpy as np
# valores = np.random.randint(0, 10, (5, 4)) #matriz 5x4 com nums aleatorios inteiros de 0 a 10, sem incluir o 10
# print(valores)
# resultado = np.where(valores < 5, valores, 10*valores) #nova matriz onde: quando os valores forem menores que 5, mantem o valor. Qnd nao, multiplica por 10
# print(resultado)

# --------------
# Where
# É possível combinar o where com conectivos lógicos
# Coloque cada condição entre parêntesis ()
# & representa um e lógico
# | representa um ou lógico

# import numpy as np

# valores = np.random.randint(0, 10, (5, 4))
# print(valores)
# resultado = np.where((valores >= 3) & (valores <= 7), valores, 10*valores) #valores iguais ou maiores que 3 e menores ou iguais a 7 são mantidos. Do contrário, multiplca0se por 10
# print(resultado)

# --------------
# Aplicando condições diretamente
# É possível aplicar condições diretamente no operador []

# import numpy as np
# valores = np.random.randint(0, 10, (5, 4))
# print(valores)
# valores[(valores < 3) | (valores == 9)] = 33 #todo valor menor que 3 ou igual a 9 será substituido por 33
# print(valores)

# --------------
# Matrizes de máscaras
# É possível ainda criar matrizes de “máscaras”, que podem ser usadas para algum pós-processamento

# import numpy as np

# valores = np.random.randint(0, 10, (5, 4))
# print(valores)
# mascara = valores < 5 #determina true ou false dependendo se o valor for menor ou não que 5
# print(mascara)
# mascara = mascara.astype(int) #reinterpreta a matriz de booleanos 'mascara = valores', como uma matriz de inteiros
# print(mascara) #o que é true vira 1 e o que é false vira 0

# ------------------
# Veja mais sobre where e operadores lógicos em
# numpy.org/doc/stable/reference/generated/numpy.where.html
# numpy.org/doc/stable/reference/routines.logic.html
# www.geeksforgeeks.org/numpy-array-logical-operations

# Ordenação e Estatística Básica

# Ordenando
# Para ordenar um array NumPy, basta chamar a função sort()

# import numpy as np
# valores = np.random.randint(0, 6, (5, 5))
# print(valores)
# valores.sort(axis=0) #axis = 0 é padrao, caso não haja, dá no mesmo. Usar o axis depende de quantas dimensões têm na matriz
# print(valores)

# --------------
# Média
# A média dos elementos pode ser computada através da função mean()
# De maneira similar, é possível calcular
#     Média ponderada: average()
#     Desvio padrão: std()
#     Variância: var()
# …
# Veja mais em
# numpy.org/doc/stable/reference/routines.statistics.html

# -------------
# Máximo e Mínimo
# As funções max() e min() podem ser usadas para se encontrar o maior e o menor valor em um Array NumPy


# ---------------
# Argmax e Argmin
# É possível encontrar o índice do maior e menor valor no array utilizando argmax() e argmin()
# Caso exista mais de uma cópia do maior/menor valor, o índice da primeira ocorrência é retornado


# -----------------
#Exemplo
# Considere o arquivo TRE-BA.csv disponibilizado
# A coluna 62 (mov_count) contém a contagem de movimentos de cada processo
# Vamos calcular:
    # A quantidade média de movimentos
    # O desvio padrão
    # O maior e menor número de movimentos
    # O índice dos (primeiros) processos com o maior e menor número de movimentos

# import numpy as np
# data = np.genfromtxt('TRE-BA.csv', delimiter=';', skip_header = 1, usecols = (62), dtype=(np.intc))
# print(data.mean())
# print(data.max())
# print(data.min())
# print(data.argmax())
# print(data.argmin())

# --------------------
# Matplotlib
# Pacote para criar gráficos
# Principalmente gráficos bidimensionais
# Projeto iniciado em 2002 por John Hunter
# Muitos dos comandos e lógicas envolvidas nos gráficos são
# compatíveis com ferramentas como MATLAB e Octave

# import matplotlib.pyplot as plt #utliza as funções do pacote pyplot do matplotlib e imprime os dados em formato de gráfico
# import numpy as np #gera os dados 

# x = np.arange(0,10,1) #cria um vetor de 0 a 10, sem incluir o 10, pulando de 1 em 1
# y = x**2 #f(x) = x^2   ===== cada valor de x é elevado ao quadrado

# plt.plot(x,y) #A função matplotlib.pyplot.plot(x,y) recebe dois vetores contendo os valores de x, e os respectivos valores de y.
# plt.show() #mostra os dados criados

# -----------------
# Multiplas Séries
# Uma das formas de se adicionar múltiplas séries, é chamando matplotlib.pyplot.plot(x,y) múltiplas vezes

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(0,10,1)
# y2 = x**2 #f(x) = x^2
# y3 = x**3 #f(x) = x^3  #cada vetor é elevado ao cubo

# plt.plot(x,y2)
# plt.plot(x,y3)
# plt.show()

# ------------------
# Estilizando
# É possível trocar as cores e estilo das linhas
# Para uma listagem completa dos estilos de cores e linhas
# matplotlib.org/3.5.1/tutorials/colors/colors.html
# matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(0,10,1)
# y2 = x**2 #f(x) = x^2
# y3 = x**3 #f(x) = x^3

# plt.plot(x,y2, "b-.")   #b- para azul (blue) com linha tracejada
# plt.plot(x,y3, "k:")    #k: para preto com linha pontilhada
# plt.show()

# -----------------
# Legendas
# É possível adicionar legendas
# Nas séries
    # Adicione a série com plt.plot(..., label = "legenda" )
    # Antes de chamar show(), configure a posição com 'plt.legend(loc="posição")'
# Veja as posições possíveis em: matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.legend.html

# Legendas nos eixos x e y podem se adicionadas através de
# plt.ylabel("Nome eixo y")
# plt.xlabel("Nome eixo x")

# import matplotlib.pyplot as plt
# import numpy as np

# x= np.arange(0,10,1)
# y2 = x**2 #f(x) = x^2
# y3 = x**3 #f(x) = x^3

# plt.plot(x,y2, "b-.", label= "x^2") #nome da legenda = x^2
# plt.plot(x,y3, "k:", label= "x^3") #nome da legenda = x^3
# plt.legend(loc="upper left") #legenda aparecerá no canto superior esquerdo
# plt.ylabel("Eixo Y") #nome do eixo = eixo y
# plt.xlabel("Eixo X") #nome do eixo = eixo x
# plt.show()

# -----------------
# Dados
# Considere os arquivos PETR3.SA.csv e PRIO3.SA.csv que contém 
    # os valores das ações da Petrobras e PetroRio entre os dias 04/01/2021 e 15/03/2022
# Os dados foram retirados de finance.yahoo.com
# Vamos considerar o preço de fechamento das ações

# import matplotlib.pyplot as plt
# from datetime import datetime #para lidar com datas
# import numpy as np

# dataPetr = np.genfromtxt('c:/users/particular/desktop/PETR3.SA.csv', delimiter=',', skip_header = 1, usecols = (0,5),  #carrega a coluna 0 e a 5
# converters={0: lambda x: datetime.strptime(x.decode('ascii'), "%Y-%m-%d")}) #pra coluna zero, usa o conversor que diz que pra cada item que receber, transforma-o para uma data, transformando-o numa string no formato ascii e essa string ta no formato '%Y-%m-%d' ano, mes e dia # type: ignore
# dias = np.empty((dataPetr.shape[0]), dtype=datetime) #arrays separados: este é o dias, criado vazio
# valores = np.empty((dataPetr.shape[0]), dtype=np.float64) #arrays separados: este é o valores, criado vazio 'empty'

# i = 0
# for d in dataPetr:
#     dias[i] = d[0] #dados da coluna 0
#     valores[i] = d[1] #dados da coluna 5
#     i += 1

# plt.plot(dias,valores, "b-.", label = "PETR3")
# plt.legend(loc="upper left")
# plt.ylabel("Preço (R$)")
# plt.xlabel("Data")
# plt.show()

# -----------------------
# Adicionando PRIO3
# import matplotlib.pyplot as plt
# from datetime import datetime
# import numpy as np

# data_petr = np.genfromtxt('c:/users/particular/desktop/PETR3.SA.csv', delimiter=',', skip_header = 1, usecols = (0,5), converters={0: lambda
# x: datetime.strptime(x.decode('ascii'), "%Y-%m-%d")})
# dias = np.empty((data_petr.shape[0]), dtype=datetime)
# valores_petr = np.empty((data_petr.shape[0]), dtype=np.float64)

# data_prio = np.genfromtxt('c:/users/particular/desktop/PRIO3.SA.csv', delimiter=',', skip_header = 1, usecols = (0,5), converters={0: lambda
# x: datetime.strptime(x.decode('ascii'), "%Y-%m-%d")})
# valores_prio = np.empty((data_prio.shape[0]), dtype=np.float64)

# i = 0
# while(i < data_petr.shape[0]):
#  dias[i] = data_petr[i][0]
#  valores_petr[i] = data_petr[i][1]
#  valores_prio[i] = data_prio[i][1]
#  i += 1

# plt.plot(dias,valores_petr, "b-.", label = "PETR3")
# plt.plot(dias,valores_prio, "k:", label = "PRIO3")
# plt.legend(loc="upper left")
# plt.ylabel("Preço (R$)")
# plt.xlabel("Data")
# plt.show()

# ----------------------
# Figure
# Manipulações mais complexas podem exigir o uso de uma variável do tipo Figure
# Retornada pela função plt.figure()

# add_subplot
# É possível adicionar sub gráficos (subplots) em uma Figure através de add_subplot(linhas, colunas, idx)
# Considerando que o gráfico completo é um grid (matriz) de NxM
    # Linhas: indica o número de linhas no grid
    # Colunas: indica o número de colunas no grid
    # Idx: índice do subgráfico no gráfico

# Adicionando em subgráficos
# Funções como plt.plot(), plt.legend(), plt.xlabel() 
    # vão criar gráficos e alterar o último subplot adicionado, somente o último

# import matplotlib.pyplot as plt
# from datetime import datetime
# import numpy as np

# data_petr = np.genfromtxt('c:/users/particular/desktop/PETR3.SA.csv', delimiter=',', skip_header = 1, usecols = (0,5), converters={0: lambda
# x: datetime.strptime(x.decode('ascii'), "%Y-%m-%d")})
# dias = np.empty((data_petr.shape[0]), dtype=datetime)
# valores_petr = np.empty((data_petr.shape[0]), dtype=np.float64)

# data_prio = np.genfromtxt('c:/users/particular/desktop/PRIO3.SA.csv', delimiter=',', skip_header = 1, usecols = (0,5), converters={0: lambda
# x: datetime.strptime(x.decode('ascii'), "%Y-%m-%d")})
# valores_prio = np.empty((data_prio.shape[0]), dtype=np.float64)

# i = 0
# while(i < data_petr.shape[0]):
#  dias[i] = data_petr[i][0]
#  valores_petr[i] = data_petr[i][1]
#  valores_prio[i] = data_prio[i][1]
#  i += 1

# fig = plt.figure() #chama a função figure retornada na variavel 'fig'
# fig.add_subplot(2, 1, 1, title= "Gráfico da Petrobras") #cria um subgrafico com 2 linhas e 1 coluna. o ultimo 1 significa que é o primeiro graifco, ficando na parte de cima
# plt.plot(dias,valores_petr, "b-.", label = "PETR3")
# plt.legend(loc="upper left")
# plt.ylabel("Preço (R$)")
# plt.xlabel("Data")

#                     #outro subgrafico, igual ao primeiro
# fig.add_subplot(2, 1, 2, title= "Gráfico da PetroRio")
# plt.plot(dias,valores_prio, "k:", label = "PRIO3")
# plt.legend(loc="upper left")
# plt.ylabel("Preço (R$)")
# plt.xlabel("Data")
# plt.show()

# ----------------------
# Tipos de Gráficos
# Existem diversos outros tipos de gráficos
    # Gráficos de barra
    # Scatter
    # Pizza
    # Boxplot
# Veja uma lista aqui matplotlib.org/3.5.1/plot_types/index.html

# Exemplo
# Mostrar como gráficos de barras os preços das ações 
    # referentes aos 30 primeiros dias das séries

# import matplotlib.pyplot as plt
# from datetime import datetime
# import numpy as np

# data_petr = np.genfromtxt('c:/users/particular/desktop/PETR3.SA.csv', delimiter=',', skip_header = 1, usecols = (0,5), converters={0: lambda
# x: datetime.strptime(x.decode('ascii'), "%Y-%m-%d")})
# dias = np.empty((data_petr.shape[0]), dtype=datetime)
# valores_petr = np.empty((data_petr.shape[0]), dtype=np.float64)

# data_prio = np.genfromtxt('c:/users/particular/desktop/PRIO3.SA.csv', delimiter=',', skip_header = 1, usecols = (0,5), converters={0: lambda
# x: datetime.strptime(x.decode('ascii'), "%Y-%m-%d")})
# valores_prio = np.empty((data_prio.shape[0]), dtype=np.float64)

# i = 0
# while(i < 30):
#  dias[i] = data_petr[i][0]
#  valores_petr[i] = data_petr[i][1]
#  valores_prio[i] = data_prio[i][1]
#  i += 1

# fig= plt.figure()
# fig.add_subplot(2,1,1)
# plt.bar(dias,valores_petr, label= "PETR3") #'plt.bar' gráfico de barras
# plt.legend(loc="upper left")
# plt.ylabel("Preço (R$)")
# plt.xlabel("Data")

# fig.add_subplot(2,1,2)
# plt.bar(dias,valores_prio, label= "PRIO3")
# plt.legend(loc="upper left")
# plt.ylabel("Preço (R$)")
# plt.xlabel("Data")
# plt.show()

# ------------------
# Salvando
# É possível salvar um gráfico através da função
    # plt.savefig("Caminho de destino")
# Substitui o 'plt.show()'

# A função infere automaticamente o tipo do arquivo pela extensão do caminho. 
    # Por exemplo, para salvar em pdf: plt.savefig("imagem.pdf")
# Veja mais em
# matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.savefig.html

# import matplotlib.pyplot as plt
# from datetime import datetime
# import numpy as np

# data_petr = np.genfromtxt('c:/users/particular/desktop/PETR3.SA.csv', delimiter=',', skip_header = 1, usecols = (0,5), converters={0: lambda
# x: datetime.strptime(x.decode('ascii'), "%Y-%m-%d")})
# dias = np.empty((data_petr.shape[0]), dtype=datetime)
# valores_petr = np.empty((data_petr.shape[0]), dtype=np.float64)

# data_prio = np.genfromtxt('c:/users/particular/desktop/PRIO3.SA.csv', delimiter=',', skip_header = 1, usecols = (0,5), converters={0: lambda
# x: datetime.strptime(x.decode('ascii'), "%Y-%m-%d")})
# valores_prio = np.empty((data_prio.shape[0]), dtype=np.float64)

# i = 0
# while(i < 30):
#  dias[i] = data_petr[i][0]
#  valores_petr[i] = data_petr[i][1]
#  valores_prio[i] = data_prio[i][1]
#  i += 1

# fig= plt.figure()
# fig.add_subplot(2,1,1)
# plt.bar(dias,valores_petr, label= "PETR3") #'plt.bar' gráfico de barras
# plt.legend(loc="upper left")
# plt.ylabel("Preço (R$)")
# plt.xlabel("Data")

# fig.add_subplot(2,1,2)
# plt.bar(dias,valores_prio, label= "PRIO3")
# plt.legend(loc="upper left")
# plt.ylabel("Preço (R$)")
# plt.xlabel("Data")
# plt.savefig("c:/users/particular/desktop/graficoaula7.pdf")

# ---------------------
# Histograma
# Um histograma geralmente é representado através de um gráfico de barras
# Gera uma aproximação visual da distribuição dos dados

# Para gerar um histograma via Matplotlib, basta chamar a função hist()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([2,1,1,4,5,5,3,4,4,5,5,5,6,7,7,7])

# plt.hist(x, bins=7,edgecolor="red") #plt.hist para mostrar o histograma, 'edgecolor="red"' = barras com laterais vermelhas 
# plt.show()

# --------------
# Bins
# Muitas vezes, desejamos agrupar os dados em bins
# Por exemplo, desejamos agrupar todos os valores entre 1 e 3
#     em uma única barra, os valores entre 4 e 6 em outra, …
# Cada agrupamento é um bin
# Bins também são conhecidos como buckets (baldes)

# import matplotlib.pyplot as plt
# import numpy as np

# data = np.genfromtxt('c:/users/particular/desktop/dados.csv', delimiter=';', skip_header = 1, usecols = (1),
# dtype=np.int32)

# plt.hist(data, bins=10,edgecolor="white") #bins = baldes do mesmo tamanho
# plt.show()

# -------------------------
# É possível ainda especificar um tamanho para cada bin, e o tamanho dos bins não precisa ser o mesmo para todos.

# import matplotlib.pyplot as plt
# import numpy as np

# data = np.genfromtxt('c:/users/particular/desktop/dados.csv', delimiter=';',
# skip_header = 1, usecols = (1), dtype=np.int32)

# plt.hist(data, bins=(0,25,50,70,80,90,100),edgecolor="white") #0 a 24 dentro de um bin, 25 a 49 noutro, 50 a 69 em outro...
# plt.show()

# ---------------------
# EXERCÍCIOS
# Questão 01
# Considere o trecho a seguir e indique o que será impresso na tela.

# import numpy as np
# x = np.arange(0, 100, 2)
# y = x[np.argmax(x)]
# print(y)

# Escolha uma opção:
# a. 50
# b. 98                RESPOSTA
# c. 100
# d. 49
# e. 99

# ---------------------
# Questão 02
# 


