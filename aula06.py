# NumPy = Numerical Python
# Biblioteca para Python para lidar com vetores e matrizes “grandes” e de múltiplas dimensões
# Mitiga muitas das ineficiências computacionais do Python quando lidando com esse tipo de dado
# Algumas vantagens:
# Estrutura de dados eficiente para armazenar e operar em arrays (vetores/matrizes)
# Funções matemáticas prontas para operar em arrays
# Funções para carga e descarga de dados de/para o disco
# Funções de álgebra, geração de números aleatórios, transformadas

# Depois de instalar o NumPy, basta importar
# Dica: instale via pip, veja o tutorial
# import numpy as np

# ---------------
# Função Array
# Os arrays NumPy são chamados de ndarrays

# import numpy as np
    # #criando a partir de uma lista
# lista = [1,2,3]
# array1 = np.array(lista)
# print("Elemento em zero: ", array1[0])
# for item in array1:
#     print(item)

    # #criando diretamente
# array2 = np.array([4,5,6])
# for item in array2:
#     print(item)

# ---------------------
# Matrizes
# É possível iterar nos itens da matriz, ou acessar diretamente via o operador []

# import numpy as np
# #criando diretamente
# array = np.array([[4,5,6],[7,8,9]])
# for linha in array:
#     for coluna in linha:
#         print(coluna, end=' ') #end = ' ' é para nao pular de linha e sim adicionar espaço entre os itens
#     print() 

# print("Item na linha 1, coluna 2: ", array[1][2])

# ----------------
# Propriedades
# Arrays NumPy possuem algumas propriedades que podem seracessadas
# Exemplos:
# dtype: qual o tipo dos dados do array
# shape: qual o formato (dimensões) do array
# size: tamanho total do array
# ndim: número de dimensões

# import numpy as np

# vetor = np.array([1.7,2,3,4])
# matriz = np.array([[4,5,6],[7,8,9]])

# print(vetor.ndim, vetor.shape, vetor.dtype, vetor.size)
# print(matriz.ndim, matriz.shape, matriz.dtype, matriz.size)

# ------------------
# Inicialização de Arrays

# Vazios e uns
# A função zeros(shape, dtype=float) preenche um vetorcom zeros
# O vetor tem dimensões shape
# A função ones(shape, dtype=float) faz o mesmo, maspreenche o vetor com uns '1'
# Por padrão os valores serão floats. O tipo dos valores pode ser modificado pelo parâmetro dtype
# Veja uma listagem de tipos válidos aqui
# numpy.org/devdocs/user/basics.types.html

# import numpy as np
# vetor_zeros = np.zeros(4) #por padrão os elementos dentro do array são float, pos isso o ponto separa os zeros no resultado
# matriz_zeros = np.zeros((3,2))
# matriz_uns = np.ones((5,5), dtype=np.intc) # 'intc' é tipo dos dados: inteiros. isso faz com que não seja floats

# print(vetor_zeros)
# print(matriz_zeros)
# print(matriz_uns)

# ----------------
# Full
# full(shape, fill_value, dtype=None) cria um vetor preenchido com fill_value
# é possivel especificar o valor que será colocado dentro da matriz
    #neste exemplo, o valor é o numero 6, transformado em inteiro através de 'intc'

# import numpy as np
# matriz_seis = np.full((5,5), 6, dtype=np.intc)
# print(matriz_seis)

# --------------
# Empty
# A função empty(shape, dtype=float) criar um array de dimensões
    # shape sem inicializar os valores, ou seja, é sua responsabilidade carregar os valores lá dentro
# Não é possível saber os valores atribuídos a cada posição do vetor
# Lixo de memória
# Custa mais barato chamar empty do que zero ou ones, por exemplo
# Útil quando precisamos criar um array que vamos preencher posteriormente

# --------------
# Arange
# A função arange(start, stop, step) retorna um vetor gerado no intervalo [start, stop)
# Inicia em start e termina em stop (sem incluir o stop)
# Cada valor entre start e stop tem uma distância step

# import numpy as np
# vetor1 = np.arange(10, 20, 2) #elementos do 10 até o 20, sem chegar no 20, pulando de 2 em 2
# print(vetor1)

# ---------------
# Linspace
# linspace(start, stop, num) retorna um vetor gerado no intervalo [start, stop]
# O vetor vai possuir num valores igualmente espaçados

# import numpy as np
# vetor2 = np.linspace(10, 20, 5) #elementos do 10 até o 20, com 5 elementos precisamente espaçados
# print(vetor2)

# -------------
# Aleatorio
# É possível preencher um array com valores aleatórios chamando
    # np.random.rand(d0, d1, ..., dn) '.rand' é a função
# d0, d1, … especifica o tamanho das dimensões do array
# Os números são gerados a partir de uma distribuição uniforme
# Os números gerados estarão no intervalo [0, 1)

# import numpy as np

# matrizRand = np.random.rand(2, 3)
# print(matrizRand)

# vetRand = np.random.rand(5)
# print(vetRand)

# -------------------
# Aleatório com inteiros
# random.randint(low, high=None, size=None) é similar a rand, mas preenche o array com valores inteiros

# import numpy as np

# dados = np.random.randint(0,100,(5,6)) #entre 0 e 100, com 5 linhas e 6 elementos
# print(dados)

# -------------------
# Outras distribuições
# Existem funções prontas para outras distribuições, como
    # Poisson: np.random.poisson(lam=1.0, size=None)
# lam é o valor de lambda
# size é uma tupla indicando as dimensões do Array

# import numpy as np

# poisson = np.random.poisson(lam=5.0, size=(2,2)) #valor de lambda e o tamanho do vetor
# print(poisson)

# -------------------
# Alterando os Arrays
# Como em listas, é possível acessar e modificar os itens diretamente através do operador []
# É possível também modificar todos os elementos do array (ou de uma única linha de uma matriz por exemplo) combinando 
    # o operador [] com os operadores:
# += X some o valor atual do elemento com X
# -= X decremente o valor atual do elemento com X
# *= X multiplique o valor atual do elemento com X
# /= X divida o valor atual do elemento com X

# import numpy as np

# matriz = np.ones((4,4), dtype=int) #vetor de 4 por 4 com numeros 1
# matriz[0][0] = 33 #trocar o elemento 0 da linha 0 por 33
# matriz += 14 #somar 14 com cada um dos elementos 
# matriz[1] *= 2 #linha 1 multiplacada por 2

# print(matriz)

# -----------------
# Reshape
# reshape
# É possível modificar as dimensões de um determinado array chamando reshape(newshape)
# A função vai retornar uma variável contendo uma visão com as dimensões rearranjadas
# As dimensões são uma tupla passada para newshape

# Exemplo

# import numpy as np

# dados = np.linspace(2, 32, 16, dtype=np.intc) #do 2 ao 32 com 16 elementos
# print(dados.shape) #mostra o formato dele, unico vetor com 16 colunas
# print(dados)

# alterado = dados.reshape((8,2)) #transforma em 8 linhas com cada linha contendo 2 colunas
# print(alterado.shape)
# print(alterado)

# -------------------
# Deduzir dimensões
# A função reshape aceita que seja atribuído -1 a uma das dimensões.
# Nesse caso, a própria função vai inferir automaticamente o valor dessa dimensão

# import numpy as np

# dados = np.linspace(2, 32, 16, dtype=np.intc)
# alterado = dados.reshape((-1,4)) #ele deduz automaticamente o numero de colunas ou se quiser, elementos

# print(alterado.shape)
# print(alterado)

# -----------------------
# Cuidado
# A função reshape retorna uma variável que contém uma nova visão, mas que compartilha os dados
# Modifica os dados de uma visão, automaticamente todas as visões que usam esses dados

# import numpy as np

# dados = np.linspace(2, 32, 16, dtype=np.intc)
# alterado = dados.reshape((-1,2))
# dados[0] = -5

# print(dados)
# print(alterado)

# -------------------
# Funções matemáticas
# Existem diversas funções matemáticas prontas para operar em arrays NumPy
# Veja uma lista aqui
# numpy.org/doc/stable/reference/routines.math.html

#Alguns exemplos

# sum
# A função sum() retorna a soma dos elementos em um array

# import numpy as np
# dados = np.ones((4,3))
# print(dados)

# soma = dados.sum()
# print(soma)

# --------------------
# Outro exemplo da sum
# Opcionalmente, pode-se definir a dimensão na qual a soma será feita sum(dim)
    # pela dimensão

# import numpy as np
# dados = np.ones((4,3)) 
# soma = dados.sum(0) #diagonal, '4'. 3 colunas
# print(soma)
# soma = dados.sum(1) #horizontal, '3' . 4 linhas
# print(soma) 

# -----------------
# outro exemplo da sum
# É possível também executar a soma para uma linha específica
# Exemplo:

# import numpy as np
# dados = np.ones((4,3))
# linha0 = dados[0].sum() #somatório da linha 0
# print(linha0) 

# ------------------
# diff
# np.diff(array) faz o cálculo array[n] - array[n-1], ou
    # seja, faz o cálculo da diferença entre os elementos com lag=1
# É possível especificar outros lags

# import numpy as np

# dados = np.random.randint(0,10,(5,6))

# print(dados)
# print(np.diff(dados))

# ----------------
# cumsum
# np.cumsum(array) faz a soma cumulativa dos elementos do array

# import numpy as np
# dados = np.ones((3,3))
# print(dados)
# print(np.cumsum(dados))

# ----------------
# Leitura de CSVs
# Existem várias formas para se carregar o CSV para o NumPy

# genfromtxt
# O NumPy possui a função np.genfromtxt(caminhoArquivo,
    # delimiter= delim, skip_header = skip, usecols = cols, dtype=tipos)
# Faz a carga automática de dados do csv
# delim: delimitador usado no arquivo
# skip: número de linhas de header a serem ignoradas
# cols: tupla com as colunas que devem ser carregadas
# tipos: tupla com os tipos das colunas

# import numpy as np
# data = np.genfromtxt('c:/users/particular/desktop/aula06.csv', delimiter=';', #caminho pro arquivo e delimitador ponto e virgula
# skip_header = 1, usecols = (13,24), dtype=(np.intc, np.intc)) #'skip_header = 1' pular a primeira pois é a do cabeçalho / 'usecols = (13,24)' = carregar colunas 13 e 24 / 'dtype=(np.intc, np.intc)' = determina que as duas colunas só terão numeros inteiros
# print(data.shape)
# print(data.sum(0)) #fazer o somatório dos elementos coluna à coluna

# ------------
# Salvando
# Para salvar um ndarray em um CSV, uma possibilidade é o uso da 
    # função np.savetxt(nomeArquivo, array, fmt= specf, delimiter=delim) 
    # specf: especificador de formato dos dados.
# Por padrão é float
# Especificadores similares a linguagem C
# numpy.org/devdocs/reference/generated/numpy.savetxt.html
# delimitador: delimitador do CSV

# import numpy as np

# dados = np.ones((3,4), dtype=np.intc)
# np.savetxt("c:/users/particular/desktop/aula06.csv", dados, delimiter=";", fmt="%d") #'%d' salva tudo como inteiro


# --------------
# Parâmetros
# Tanto genfromtxt quanto savetxt possuem diversos parâmetros extras que podem te ajudar em tarefas específicas.
# Por exemplo, se você deseja adicionar um header, utilize o parâmetro de mesmo nome
# Dica: Os headers e footers são inseridos por padrão como comentários
# Para alterar isso, coloque comments=""

import numpy as np
dados = np.ones((3,4), dtype=np.intc) #criada a matriz de 3 por 4 com elementos 1 
header = "Coluna0;Coluna1;Coluna2;Coluna3" #criado o header
np.savetxt("c:/users/particular/desktop/aula06.csv", dados, delimiter=";", fmt="%d", header=header, comments="") #não os coloque como comentários

#--------------------------------------
# EXERCÍCIOS
# Questão 01
# Ao executar o trecho a seguir, o que será armazenado na variável vetor1?

# import numpy as np
# vetor1 = np.arange(-2, 10, 1)
# print(vetor1)


# Escolha uma opção:
# a. [-2 -1  0  1]
# b. [-2 -1  0]
# c. [-2 -1  0  1  2  3  4  5  6  7  8  9 10]
# d. [-2 -1  0  1  2  3  4  5  6  7  8  9]    RESPOSTA
# e. [-1  0  1  2  3  4  5  6  7  8  9]

# -------------
# Questão 02
# Ao executar o trecho a seguir, o que será armazenado em vetor2?

# import numpy as np
# vetor2 = np.linspace(5, 6, 9)

# print(vetor2)

# Escolha uma opção:
# a. [ 5.     5.625  6.25   6.875  7.5    8.125  8.75   9.375]
# b. [5.0         5.11111111 5.22222222 5.33333333 5.44444444 5.55555556  5.66666667 5.77777778 5.8888888]
# c. [5.0    5.125 5.25  5.375 5.5   5.625 5.75  5.875]
# d. [5.0    5.125 5.25  5.375 5.5   5.625 5.75  5.875 6.0 ]        RESPOSTA
# e. [ 5.0     5.625  6.25   6.875  7.5    8.125  8.75   9.375 10.0 ]

# -----------------
# Questão 03
# Considere um arquivo chamado dados.csv com as seguintes três linhas de conteúdo
# 1;2;3
# 1;2;3
# 1;2;3
# Ao executar o programa a seguir, o que será impresso na tela?

import numpy as np
dados = np.genfromtxt("dados.csv", delimiter=';', skip_header= 0, dtype=np.intc)

resultado1 = dados[1].sum()
resultado2 = dados.sum(0)[2]

print(resultado1, resultado2)


# Escolha uma opção:
# a. 18 9
# b. 9 6
# c. 3 6 9
# d. 6 9
# e. 6 6