# STRINGS
# Assim como para listas convencionais, a função len() vai retornar o tamanho da string (o número de caracteres)

# frase = "Curso de Python"
# print("Num caracs:", len(frase))

#--------

# Acessando caractere numa posição especifica
# print(frase[2])

# ----------
# Acessando os caracteres partindo de uma posição ate outra

frase = "Curso de Python"
print("Primeira Letra:", frase[0]) # Primeira letra

linguagem = frase[3:len(frase)] # até o final da string
print("Do caractere 3 até o final: ", linguagem)

print(frase[1:3]) # do caractere 1 até o 2, pois o 3 não é incluso

# -----------
# Replace
