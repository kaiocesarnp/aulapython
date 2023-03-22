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
