# DICIONÁRIOS

# Um dicionário é uma coleção não-ordenada de “valores” indexados por “chaves” {}.
# Dicionários se parecem com listas, mas são mais versáteis

# dic = {'chave1':'valor1','chave2':'valor2'}
# print(dic['chave2'])

# ------------------------

#Criando uma nova chave:
    # Pode-se também atribuir um novo valor, caso já exista esta chave no dicionário
# dic['chave3'] = 'valor3'
# print(dic)

# ------------------------

# Removendo um elemento
# dic.pop('chave1')
# print(dic)

# ----------------------

# Removendo o último elemento
# dic.popitem()
# print(dic)

# --------------------

# Removendo elemento especifico
# del dic['chave2']
# print(dic)

# ----------------------

# Removendo o dicionário completo
# del dic
# print(dic)

# --------------------------------------------------------------

# IMPRESSÃO DE DICIONÁRIOS E MÉTODOS

# dic1 = {'banheiro': 3, 'sala': 2, 'quarto': 4}

# print(dic1)
# print(len(dic1)) #ver o tamanho do dicionario

# ----------------------
# imprimindo os elementos individualmente:
# for chave in dic1:
#     print(chave)

# ------------------------
# imprimindo os valores
# for chave in dic1:
#     print(dic1[chave])

# -----------------------
# imprimindo tudo em linhas separadas
# for chave in dic1:
#     print(chave, dic1[chave])

# ------------------------
# Pegando a lista de todas as chaves que tem no dicionário
# dic2 = {'guarda-roupa': 3, 'televisão': 2, 'cadeira': 4, 'mesa': 1}
# dic2.keys()

# ----------------------
# Pegando os valores da lista
# dic = {'guarda-roupa': 3, 'televisão': 2, 'cadeira': 4, 'mesa': 1}
# dic.values()

# -----------------------
# Associar o indice com o valor associado à chave que serve de indice
# dic = {'guarda-roupa': 3, 'televisão': 2, 'cadeira': 4, 'mesa': 1}
# dic.items()

# --------------------

# ORDENAÇÃO DE DICIONÁRIOS

# Os elementos do dicionario em python são apresentados na ordem que são inseridos
# dicio = {}

# dicio [2] = "b"
# dicio [1] = "a"
# dicio [3] = "c"

# print(dicio)

#-----------------------
# Com a função 'sorted' é possivel ordernar, desde que os itens sejam comparaveis
# dicio = {'quarto':3, 'sala':2, 'banheiro':5}
# dicio = (dict(sorted(dicio.items())))
# print(dicio)

# -----------------------
# Ordenar por valor
    # Cria-se um novo dicionario vazio
        # Utilizando 'key=dicio.get' no metodo 'sorted', os valores são usados para ordenar

# dicio = {2: 'f', 1: 'x', 3: 'b'}
# dic_ordenado = {}
# chaves_ordenadas = sorted(dicio, key=dicio.get)

# for i in chaves_ordenadas:
#     dic_ordenado[i] = dicio[i]

# -------------------------

# MATRIZES
# Enquanto um array é uma estrutura para armazenar dados de forma “linear”, uma matriz é um array bi-dimensional.
# Um array bi-dimensional é um array dentro de outro array.
# Todas as operações feitas em um array podem ser feitas usando listas…

# matriz = [ [4, 5, 6], [7, 8, 9]]
# print(matriz[1]) #acessar a lista
# print(matriz[0][2]) #acesssar o elemento 

# print(type(matriz))

# ---------------------
# MANIPULANDO MATRIZES

# Inserindo elementos no final
# matriz = [ [4, 5, 6], [7, 8, 9]]
# matriz.append([10, 11, 12])
# print(matriz)

# ---------
# Inserção posicional em matriz
# matriz = [ [4, 5, 6], [7, 8, 9]]
# matriz.insert(1, [12, 14, 15])
# print(matriz)

# ---------
# Atualizando uma matriz (troca lista)
# matriz = [ [4, 5, 6], [7, 8, 9]]
# matriz[0] = [-4, 10, -7]
# print(matriz)

# -----------
# Atualizando um elemento especifico (substitui dado)
# matriz = [ [4, 5, 6], [7, 8, 9]]
# matriz [0][2] = 164
# print(matriz)

# -----------
# Removendo um linha (apaga uma lista)
# matriz = [ [4, 5, 6], [7, 8, 9]]
# del(matriz[1])
# print(matriz)

# ----------
# Removendo um elemento especifico
# matriz = [ [4, 5, 6], [7, 8, 9]]
# del(matriz[0][1])
# print(matriz)

# ---------
# Tamanho de uma matriz
# matriz = [ [4, 5, 6], [7, 8, 9]]
# tamanho = len(matriz)
# print(tamanho)

# ----------------------
# SUBMATRIZES E COPIAS DE MATRIZES

# Fatiamento de uma matriz

# matriz = [ [0,1,2], [3,4,5], [6,7,8], [9, 10, 11], [12, 13, 14], [15, 16, 17]]

# matriz2 = matriz[1:5] # pega do indice 1 e vai até o menor que 5
# print(matriz2)

# -------
# Outra forma
# matriz = [ [0,1,2], [3,4,5], [6,7,8], [9, 10, 11], [12, 13, 14], [15, 16, 17]]

# matriz2 = matriz[2:] # quando não se define o final, vai até o final
# print(matriz2)

# ----------
# Outra forma
# matriz = [ [0,1,2], [3,4,5], [6,7,8], [9, 10, 11], [12, 13, 14], [15, 16, 17]]

# matriz2 = matriz[:2] # do inicio até uma posição definida, menor que 2 no caso
# print(matriz2)

# --------------------------
# Copia de uma matriz, sem modificar
import copy
m1 = [[1, 1], [2,2]]
m2 = copy.copy(m1)
m1[0] = [0,0]

print(m1)
print(m2)