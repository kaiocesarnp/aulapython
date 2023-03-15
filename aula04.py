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



