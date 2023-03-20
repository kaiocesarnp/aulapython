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

# Formatando Strings
# Existem várias formas para formatar uma string
# Uma delas é usar a função format()
# A forma mais simples de usar o format, é colocando {} na string.
# As chaves servem como placeholders, e serão substituídas pelo format()
# A função format() retorna uma nova string como conteúdo substituído
# Exemplo:

# anterior = 5000
# atual = 5500
# diferenca = atual - anterior
# pct = diferenca/anterior * 100
# frase = "A diferença de salário é de R${}, ou seja, {}%"
# formatado = frase.format(diferenca, pct)
# print(formatado)

# ----------
# É possível formatar diretamente no print. Veja um exemplo:

# anterior = 5000
# atual = 5500
# diferenca = atual - anterior
# pct = diferenca/anterior * 100

# formatado = "A diferença de salário é de R${}, ou seja, {}%".format(diferenca, pct)
# print(formatado)

# -----------
# outra forma

# anterior = 5000
# atual = 5500
# diferenca = atual - anterior
# pct = diferenca/anterior * 100

# print("A diferença de salário é de R${}, ou seja, {}%".format(diferenca, pct))

# ---------------
# O format infere automaticamente o tipo da variável. Mas é possível forçar um tipo específico
#  Exemplo: use {:f} para imprimir como um float

# anterior = 5000
# atual = 5500
# diferenca = atual - anterior
# pct = diferenca/anterior * 100

# print("A diferença de salário é de R${:f}, ou seja, {:.2f}%".format(diferenca, pct)) # '.2f' limita o número de casas decimais

# -------------
# Arquivos e Leitura
# Para abrir um arquivo texto em modo leitura, use a função
# arq = open(nomeArquivo, "r")
# arq é uma variável que vai representar o arquivo aberto
# "r" de read indica que o arquivo vai ser de leitura
# É obrigatório que o arquivo seja fechado depois de usando arq.close()

# Exemplo:
# arq = open("documento.txt", "r")
# #Faz algo com o arquivo
# arq.close()

# ----------
# Função read()
# A função read() lê todo o conteúdo do arquivo
# arq = open("c:/users/particular/desktop/parapyt.txt", "r")
# conteudo = arq.read()
# print(conteudo)
# arq.close()

# -----------
# Readline
# Para ler uma única linha do arquivo, utilize readline()
    # A função retorna a próxima linha do arquivo, ou uma string vazia se o arquivo terminou

# arq = open("c:/users/particular/desktop/parapyt.txt", "r")
# conteudo = arq.readline()
# while(conteudo != ""):
#     print("Linha lida:", conteudo)
#     conteudo = arq.readline()
# arq.close()

# ---------------
# Iterando
# É possível iterar linha a linha em um arquivo
    # Mas cuidado: um arquivo não é uma lista
# arq = open("c:/users/particular/desktop/parapyt.txt", "r")
# for linha in arq: #o 'readline' está implicito aqui, sendo executado da mesma forma
#     print("Linha lida:", linha)
# arq.close()

# ------------
# arq = open("c:/users/particular/desktop/parapyt.txt", "r") #lê o arquivo
# for linha in arq:           #pega o arquivo linha à linha 
#     quebra = linha.split(" ")
#     nome = quebra[0]        #nome da pessoa é o indice 0 
#     idade = int(quebra[1])  #idade é o indice 1, o 'int' transforma a string em inteiro

#     print(nome, "tem", idade, "anos de idade")
# arq.close()

# ----------------
# Modo Escrita
# Para abrir um arquivo texto em modo escrita, existem dois modos básicos
# Modo escrita (write). Se o arquivo já existir, será substituído
# f = open(nomeArquivo, "w")
# Modo anexagem (append). O conteúdo é anexado no final do arquivo, caso o arquivo já exista
# f = open(nomeArquivo, "a")

# Para escrever no arquivo, use a função write()
# Dicas:
# write() não adiciona uma quebra de linha automaticamente no texto, utilize entao '\n'
# write() só aceita strings. Converta para string usando, por exemplo
    #str() o conteúdo a ser escrito quando necessário

valor = 10
pi = 3.14
nome = "Maria da Silva"
arq = open ("c:/users/particular/desktop/parapyt2.txt", "a")
arq.write(str(valor))
arq.write(';')
arq.write(str(pi))
arq.write(';')
arq.write('\n')
arq.write(nome)
arq.write('\n')
arq.close()

# ---------------



