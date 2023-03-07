#essa é uma linha de comentário. Jogo da velha serve para comentar no python

# letra = 'a'
# print(10*letra)

# nome = input("Digite seu nome: ")
# idade = int(input("Qual a sua idade?: "))
# aposentadoria = int(input("Com qual idade você espera se aposentar?: "))
# anos_faltantes = aposentadoria - idade
# print(nome, "faltam", anos_faltantes, "anos para você se aposentar!")

# import math
# num = int(input("Digite um numero inteiro: "))
# raiz = math.sqrt(num)
# print("A raiz de", num, "é", raiz)

# Quetão 3 
# Considere o seguinte programa

# import copy
# m1 = [ [0, 0], [1, 1], [2, 2] ]
# m2 = copy.copy(m1)
# m1[0][0] = 5
# # m1[1] = [-9, -9]
# print(m2)

# Escolha uma ou mais:
# a. Após o comando m1[1] = [-9, -9], se imprimirmos m1, a saída será:
# [[5, 0], [1, 1], [-9, -9]]

# b. Para não correr riscos de modificar m2 com alterações feitas em elementos de m1, o correto seria usar o comando:
# m2 = copy.deepcopy(m1)

# c. Após o comando m1[1] = [-9, -9], se imprimirmos m2, a saída será:
# [[5, 0], [1, 1], [-9, -9]]

# d. Se colocar um comando print(m2) logo após m1[0][0] = 5, a saída será:
# [[0, 0], [1, 1], [2, 2]]

# -------------------------

# Questão 04
# Considere o seguinte script Python. Ao executar o script, o que exatamente é exibido na tela?

# import math

# nome = "Maria"
# sobrenome = "Silva"
# calculo = 36
# calculo = math.sqrt(36)
# print("nome ", nome, "sobrenome ", sobrenome, calculo)

#----------------------------- 

# Questão 05
# Considere os seguintes comandos executados no interpretador Python, 
# e indique qual o tipo das variáveis depois de todos os comandos terem sido executados.

# carro = 1
# var2 = 3
# var2 = 2.5
# var3 = 4
# var1 = "var2"

# type(carro)
# type(var2)
# type(var3)

# -----------------------

# Questão 06
# Considere os seguintes comandos executados no interpretador Python, 
# e indique qual o valor armazenado nas variáveis depois de todos os comandos terem sido executados.

# variavel1 = 10
# variavel1 = variavel1 + 2
# variavel2 = variavel1 - 1
# variavel2 = variavel1 + 10
# variavel1 + 10
# variavel2 + 1

# print(variavel1, variavel2)

# -------------------------

# Questão 09

# import pandas as pd
# import matplotlib.pyplot as plt

# dados = {'T1': [1, 0, 2], 'T2': [0, 3, 0], 'T3': [1, 1, 1]}

# df = pd.DataFrame(dados)
# df.plot(kind='bar')
# plt.show()