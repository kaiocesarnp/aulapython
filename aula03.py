# 01. Listas
#OS itens vão se manter na ordem que você definiu;
# Exceto se vc explicitamente pedir para que a ordem se alterada
# Como listas possuem multiplos itens, utilize um nome no plural



# lista_compras = ["maçãs", "leite", "arroz", "frango", "banana"]

# for item in lista_compras:
#     print("Comprar:", item)

# O primeiro elemento de uma lista é o 0 (zero)
# print("O primeiro elemento é:", lista_compras[0])
# print("O primeiro terceiro é:", lista_compras[2])

# A função 'len' mostra o tamanho da lista
# tamanho = len(lista_compras)
# print("Tamanho:", tamanho)

# Pode-se usar o tamanho 'len' da lista para acessar o ultimo elemento da lista, por exemplo
# print("Ultimo:", lista_compras[len(lista_compras)-1])

# for i in range(len(lista_compras)):
#     print("O elemento", i, "da lista é", lista_compras[i])

# i = 0
# while i < len(lista_compras):
#     print("O elemento", i, "da lista é", lista_compras[i])
#     i = i + 1
    
# Pegando uma parte da lista/intervalo
# sublista = lista_compras[1:4]
# print("Sublista")
# for item in sublista:
#     print(item)

# print("Outra forma")
# for item in lista_compras[2:6]:
#     print(item)

# Alterando item da lista
# lista_compras[0] = "batatas"
# lista_compras[1] = "laranjas"

# for item in lista_compras:
#     print(item)

#-------------

# -----------------------------FUNÇÕES DE LISTAS-------------------------

    # Indices e contagens

# função 'count' conta quantas vezes determinado elemento aparece na lista
# função 'index' mostra em qual indice da lista o elemento se encontra 
        # nessa chamada que será passada, o 'index' retornará o primeiro indice

# lista_compras = ["maças", "leite", "arroz", "frango", "leite", "trigo"]

# qtde_vezes = lista_compras.count('leite')
# idx = lista_compras.index('leite')

# print("Quantidade: ", qtde_vezes)
# print("Primeiro idx: ", idx)

# -------------------

# Função 'sort' ordena a lista... como são todas strings, nesse caso será em ordem alfabetica

# lista_compras = ["maças", "leite", "arroz", "frango", "trigo"]

# # lista_compras.sort()
# lista_compras.sort(reverse=True) # reverse=True inverte a ordem

# print("Lista:")
# for item in lista_compras:
#     print(item)

#-------------------------

# Função 'del' exclui um elemento da lista por indice

# lista_compras = ["maças", "leite", "arroz", "frango", "trigo"]

# del lista_compras[1]
# for item in lista_compras:
#     print(item)

# ------------------------------

# Função "remove(conteudo)" remove o PRIMEIRO elemento com o conteudo especificado
# Função "pop()" remove o último elemento da lista

# lista_compras = ["maças", "leite", "arroz", "arroz", "frango", "trigo"]

# lista_compras.remove("arroz")
# lista_compras.pop()
# for item in lista_compras:
#     print(item)

# ------------------------------

# Função "insert(idx, item)" insere o item na posição
# Função "append(item)" insere o item no final da lista

# lista_compras = ["maças", "leite", "arroz", "frango", "trigo"]

# lista_compras.insert(2, "feijão")
# lista_compras.append("tomate")

# for item in lista_compras:
#     print(item)

