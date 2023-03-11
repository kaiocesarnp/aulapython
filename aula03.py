# 01. Listas
#OS itens vão se manter na ordem que você definiu;
# Exceto se vc explicitamente pedir para que a ordem se alterada
# Como listas possuem multiplos itens, utilize um nome no plural



lista_compras = ["maçãs", "leite", "arroz", "frango"]

for item in lista_compras:
    print("Comprar:", item)

# O primeiro elemento de uma lista é o 0 (zero)
print("O primeiro elemento é:", lista_compras[0])
print("O primeiro terceiro é:", lista_compras[2])

# A função 'len' mostra o tamanho da lista
tamanho = len(lista_compras)
print("Tamanho:", tamanho)

# Pode-se usar o tamanho 'len' da lista para acessar o ultimo elemento da lista, por exemplo

    