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
