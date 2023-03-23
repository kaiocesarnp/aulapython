# NumPy - Operações Lógicas

# Where
# A função numpy.where(condition, resultado_if, resultado_else) retorna um array com 
    #os elementos que satisfazem determinada condição
# condition é a condição
# resultado_if são os elementos selecionados quando a condição é satisfeita
# Resultado_else são os elementos selecionados quando a condição não é satisfeita

import numpy as np
valores = np.random.randint(0, 10, (5, 4)) #matriz 5x4 com nums aleatorios inteiros de 0 a 10, sem incluir o 10
print(valores)
resultado = np.where(valores < 5, valores, 10*valores) #nova matriz onde: quando os valores forem menores que 5, mantem o valor. Qnd nao, multiplica por 10
print(resultado)