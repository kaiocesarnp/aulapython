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

frase1 = "CURSO de Python"
print(frase1.upper())
print(frase1.lower())
print(frase1.capitalize())