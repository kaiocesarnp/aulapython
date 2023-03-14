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

#--------------------------------

# Criando uma lista vazia

# lista_compras = [] # lista vazia

# item = input("Digite um item ou sair: ")
# while item != "sair":
#     lista_compras.append(item)
#     item = input("Digite um item ou sair: ")

# for it in lista_compras:
#     print(it)

# -------------------------------

# Listas são heterogeneas em Python, ou seja, pode misturar todo tipo de item:
    # inteiros, strings, outras listas...

# lista_inteiros = [1,2,3]
# elementos = ["casa", 1, "banana", lista_inteiros]

# for item in elementos:
#     print(item, type(item))

# --------------------------------
# Arrays
# Em Python, arrays são homogeneos, ou seja, todos elementos precisam ser do mesmo tipo
    # por exemplo, um array com string, só pode ter strings

# --------------------------------

# TUPLAS

# Tuplas em Py são similares a listas, no entanto são imutáveis
    # Depois de criada, você não pode fazer modificações, como por exemplo excluir algum item
    # Ao invés de colchetes [], em tuplas se usa parentese ()

# tupla_compras = ("maças", "leite", "arroz", "frango", "tigo")
# for item in tupla_compras:
#     print(item)

# print("O item 1 é", tupla_compras[1])

# --------------------

# Outro exemplo
    # 'getsizeof' essa função da biblioteca 'sys' lê o elemento e diz quantos bytes 
        # ele está ocupando na memória

# import sys

# lista = ["maças", "leite", "arroz", "frango", "tigo"]
# tupla = ("maças", "leite", "arroz", "frango", "tigo")

# print("Tamanho na memória da lista:", sys.getsizeof(lista))
# print("Tamanho na memória da tupla:", sys.getsizeof(tupla))

# ------------------------

# FUNÇÕES

# É possível criar suas próprias funções, com o comando 'def'

# def nome_funcao(): #nome da função
#     instrucao1   #instruções que definem o que a função faz
#     instrucao2

#     instrucaoN

# Exemplo:

# def saudacao():
#     print("Olá, bem vindo.")
#     print("Esse é o curso de Python")

# saudacao() #chama a função, igual 'print'

# -------------------

# PARAMETROS
# Uma função comumente possui parametros
    # Passamos esses parametros para a função, indicando o que ela precisa fazer
    # Separa-se por virgulas os parametros dentro da função

# def saudacao(nome, periodo):
#     if(periodo == 'm'):
#         print("Bom dia", nome + '.')
#     elif(periodo == 't'):
#         print("Boa tarde", nome + '.')
#     elif(periodo == 'n'):
#         print("Boa noite", nome + '.')
#     else:
#         print("Ops, período inválido")
    
#     print("Esse é o curso de Python")

# saudacao("Paulo", 't')

# ---------------------

# Valores default

# Os parametros da função podem ter valores default(padrão)
# Ao chamar a função, caso nao seja passado esse parametro, o interpretador vai
    # assumir o parametro default
# Para adicionar um valor padrão ao parametro, basta usar 'nome_par = valor_padrao'

# def saudacao(nome = 'Joao', periodo = 'm'):
#     if(periodo == 'm'):
#         print("Bom dia", nome + '.') #Essa é a saudação padrao
#     elif(periodo == 't'):
#         print("Boa tarde", nome + '.')
#     elif(periodo == 'n'):
#         print("Boa noite", nome + '.')
#     else:
#         print("Ops, período inválido")
    
#     print("Esse é o curso de Python")

# saudacao()

# ---------------------------

# FATORIAL

# Criar sua própria função para calcular fatorial de determinado número
# def fatorial(n):
#     res = 1
#     while(n > 1):
#         res = res*n
#         n = n -1
#     print("O fatorial é", res)

# valor = int(input("Digite um valor ou -1 para sair: "))
# while(valor != -1):
#     fatorial(valor)
#     valor = int(input("Digite um valor ou -1 para sair: "))

# ----------------------------

# Mais sobre FATORIAL
# A função fatorial imprime o resultado
# Isso (geralmente) é uma má prática. Idealmente, essa função deveria
# retornar (devolver) o resultado da conta.
# Quem chamou a função decide o que fazer com esse resultado.

# RETURN
# Para retornar um resultado, utilize a palavra chave 'return' dentro de uma função
# Uma função retorna (termina) imediatamente ao encontrar um return'.
# Formato: 'return valor_a_ser_retornado'

# def fatorial(n):
#     if (n < 0):
#         return -1 #retornando -1 para indicar um erro
#     res = 1
#     while(n > 1):
#         res = res*n
#         n = n -1
#     return res

# valor = int(input("Digite um valor ou -1 para sair: "))
# while(valor != -1):
#     resultado = fatorial(valor)
#     print("Fatorial de", valor, "é", resultado)
#     valor = int(input("Digite um valor ou -1 para sair: "))

# --------------------

# CÓPIAS E REFERÊNCIAS
# Variáveis simples (e.g., ints e floats) e também strings são passadas por cópia
# Isso significa que se a função alterar o parâmetro, a variável original não vai ser alterada

# Variáveis simples 
# def altera_simples(val_int, val_float, texto):
#     val_int = val_int + 1
#     val_float = val_float + 1
#     texto = texto + " teste"
#     print("Dentro da função: ", val_int, ",", val_float, ",", texto)

# meu_int = 10
# meu_float = 3.14
# minha_str = "aula"
# altera_simples(meu_int, meu_float, minha_str)
# print("Originais: ", meu_int, ",", meu_float, ",", minha_str)

# ---------------------

# Objetos compostos, como listas e arrays, são passados por referência
# Alterar o objeto na função também altera o original

# Objetos compostos
# def altera_lista(lista):
#     lista[0] = 0
#     lista[1] = 1

# def imprime_lista(lista):
#     for item in lista:
#         print(item)

# minha_lista = [3,4,5]

# print("Antes de alterar")
# imprime_lista(minha_lista)
# altera_lista(minha_lista)

# print("Depois de alterar")
# imprime_lista(minha_lista)

# ----------------------

# ATIVIDADE

# QUESTÃO 01
# Considere a função a seguir, e indique o que a função faz.
    # Assuma que o parâmetro lista sempre vai ser uma lista com 2 ou mais elementos.

# def funcao(lista):
#        fim = len(lista)-1
#        inicio = 0
#        while(inicio < fim):
#                aux = lista[inicio]
#                lista[inicio] = lista[fim]
#                lista[fim] = aux
#                inicio = inicio + 1
#                fim = fim - 1

# ---------------------------

# QUESTÃO 02
# Considere o trecho a seguir com uma função e sua chamada. Indique o que será impresso na tela.

# def minha_funcao(valor):
#         if(valor == 1):
#                 return valor + 1;
#         valor = valor + 10
#         return valor + 20

# a = 1
# resultado = minha_funcao(a)
# print(resultado)

# ----------------------------

# QUESTÃO 03
# Considere o seguinte trecho de um programa em Python e indique o que acontece com a execução do programa.

# objeto = ("cadeira", "mesa", "vaso")
# objeto.remove("cadeira")
# objeto.append("caneta")
# del objeto[0]

# for item in objeto:
#     print(item)

# --------------------------
# QUESTÃO 04
# Considerando as funções a seguir e suas chamadas, indique o que será impresso na tela.

# def funcao(a, b):
#         a = a + 1
#         b[1] = a
    
# def imprimir(lista):
#         for item in lista:
#                 #o end = seguido de duas aspas simples serve para não pular de linha
#                 print(item, ' ', end= '')
#         print()

# var = 10
# lista = [1,2,3]
# funcao(var, lista)
# print(var)
# imprimir(lista)

# ---------------------------------

# QUESTÃO 05
# Considere o programa Python a seguir. 
# Marque a alternativa que contém os itens da lista depois de executar o programa.

# lista = [1,2,58,10,19,30,58,100]
# lista.remove(58)
# del lista[1]
# lista.append(-3)
# lista.insert(2, 77)
# lista.insert(2, 77)

# print(lista)