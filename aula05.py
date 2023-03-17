# STRINGS
# Assim como para listas convencionais, a função len() vai retornar o tamanho da string (o número de caracteres)

# frase = "Curso de Python"
# print("Num caracs:", len(frase))

#--------

# Acessando caractere numa posição especifica
# print(frase[2])

# ----------
# Acessando os caracteres partindo de uma posição ate outra

# frase = "Curso de Python"
# print("Primeira Letra:", frase[0]) # Primeira letra

# linguagem = frase[3:len(frase)] # até o final da string
# print("Do caractere 3 até o final: ", linguagem)

# print(frase[1:3]) # do caractere 1 até o 2, pois o 3 não é incluso

# -----------
# Replace
# É possível substituir um trecho de uma frase por outro via 'replace' ("texto antigo", "novo")
# A  função retorna uma nova string alterada
    # A string original não é alterada

# frase = "Esse é o curso de linguagem C++. Você pode criar programas em C++."
# mudanca = frase.replace("C++", "Python", 1) # este numero signica o numero max de substituições
# print(frase)
# print(mudanca)

# ------------
# Concatenar
# É possível concatenar strings utilizando o operador +

# nome_curso = "Python"
# ola = "Bom dia."
# frase = ola + " Esse é o curso de " + nome_curso + "."
# print(frase)

# ------------
# Caracteres de controle
# Caracteres de controle “fazem algo”, sem necessariamente imprimir algo na tela
    # Em Python, um caractere de controle começa com uma barra invertida \
        # Exemplos:
        # "\n" insere uma quebra de linha
        # "\t" insere uma tabulação
# frase = "Esse é um texto\nde\t exemplo"
# print(frase)

# -------------
# Caixa
# É possível transformar a caixa dos caracteres de uma string para:
# Minúsculo usando: lower()
# Maiúsculo usando: upper()
# Primeira maiúscula e demais minúsculas: capitalize()

# frase1 = "CURSO de Python"
# print(frase1.upper())
# print(frase1.lower())
# print(frase1.capitalize())

# ------------
# Split
# Utilize split(string_de_quebra) para “quebrar” uma string em uma lista de strings

# frase = "Esse é o curso de Python - Foco em iniciantes"
# # lista1 = frase.split(" ") #itens separados por espaços
# # for item in lista1:
# #     print(item)

# lista2 = frase.split("-") #itens separados por traço
# for item in lista2:
#     print(item)

# ------------
# Índice
# Para encontrar o índice de uma palavra ou caractere, use a função find()

# frase = "Olá mundo teste isso vai ficar teste final"
# inicio = frase.find("teste") + len("teste") #len tira o item final
# fim = frase.find("teste", inicio)
# fim = frase.find("teste", inicio+1) # +1 significa a partir do primeiro que foi encontrado, sem o "+ len("teste")" 
# print(frase[inicio:fim])

# ---------------
# Lista de Funções
# Essas são apenas algumas das funções. 
# Veja uma lista mais completa em: www.w3schools.com/python/python_ref_string.asp 16
# count() Quantas vezes a palavra aparece
# endswith() Verifica se a string termina com determinada palavra
# startswith() Verifica se a string começa com determinada palavra
# islower() Verifica se todos caracteres estão em caixa baixa
# isnumeric() Verifica se todos caracteres são numéricos
# isspace() Verifica se todos os caracteres são espaços em branco
# strip() Remove caracteres em branco do começo da string
# isascii() Verifica se todos os caracteres são ASCII

# ----------------------------------------------------
