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

# valor = 10
# pi = 3.14
# nome = "Maria da Silva"

# arq = open ("c:/users/particular/desktop/parapyt2.txt", "a")

# arq.write(str(valor))
# arq.write(';')
# arq.write(str(pi))
# arq.write(';')
# arq.write('\n')
# arq.write(nome)
# arq.write('\n')
# arq.close()

# ---------------
# Arquivos Delimitados

# Você pode criar seu próprio padrão de arquivos
# Mas em sistemas simples é comum a utilização de padrões já
    # conhecidos e aceitos, como csv, xml, Json, …

# CSV - comma-separated values
# Tipo de arquivo de texto delimitado
# Os valores são separados por vírgula
    # Muitas vezes usamos outros separadores, como ';'
# Ex:
# Nome;Idade;Salário  - Um cabeçalho para ajudar a identificar as colunas
# Maria Silva;45;8500,85
# José Oliveira;30;5500,4
# Marcos Santos;35;8000 - Utilizando ';' como separador para não confundir com a vírgula dos salários
# Ex:

# arq = open("c:/users/particular/desktop/parapyt3.csv", "r")
# arq.readline()#descartando primeira linha

# idades = 0
# salarios = 0
# qtde = 0

# for linha in arq:
#  quebra = linha.split(';')
#  idades = idades + int(quebra[1])
#  salarios = salarios + float(quebra[2].replace(',','.')) #substitui a virg por ponto e em 'float'
#  qtde = qtde + 1
# arq.close()
 
# print("A idade media é", idades/qtde)
# print("O salário médio é", salarios/qtde)

# --------------
# Biblioteca padrão para CSVs
# O Python conta com uma biblioteca padrão para leitura de CSVs

# import csv

# arq = open("c:/users/particular/desktop/parapyt3.csv", "r")
# csv_reader = csv.reader(arq, delimiter = ';') #cria um leitor de csv baseado no arquivo abeto acima, com o delimitador ponto e virgula ';'

# next(csv_reader)#pular a primeira linha, no caso o cabeçalho

# idades = 0
# salarios = 0
# qtde = 0
# for linha in csv_reader: #com a criação do leito de csv, essa linha deixa de ser uma string e vira automaticamente uma lista, sem a necessidade do 'split(;)'
#  idades = idades + int(linha[1])
#  salarios = salarios + float(linha[2].replace(',','.'))
#  qtde = qtde + 1
# arq.close()

# print("A idade media é", idades/qtde)
# print("O salário médio é", salarios/qtde)

# ----------------------------------------
# EXERCÍCIOS
# Questão 01
# Considere o seguinte programa em Python e indique qual será o conteúdo do arquivo documento.txt ao final da execução do programa.

# arq = open("c:/users/particular/desktop/documento.txt", "a")
# arq.write("Olá mundo\n")
# arq.write("Cruel\n")
# arq.close()

# arq = open("documento.txt", "w")
# arq.write("Esse é um doc de texto")
# arq.close()

# Escolha uma opção:
# a. Não é possível saber o conteúdo exato do arquivo. O resultado depende do conteúdo anterior do arquivo.
# b. Olá mundo           
# Cruel
# c. Esse é um documento de texto   Resposta
# d. O programa resulta em um erro de execução e o arquivo não é escrito.

# ------------------
# Questão 02
# Ao executar os comandos a seguir, o que será impresso na tela?

# frase1 = "laranja laranja"
# frase2 = frase1.replace("laranja", "banana", 1)
# frase3 = frase1 [0:3] + " " + frase1 + " " + frase2

# print(frase3)
 
# Escolha uma opção:
# a. ban banana banana banana banana
# b. ban banana laranja banana laranja
# c. ban banana laranja banana laranja
# d. lar laranja laranja banana laranja     Resposta
# e. lara laranja laranja banana laranja

# ----------------------
# Questão 03
# Considere que matrizes estão sendo armazenadas em arquivos .csv, onde o separador é a vírgula.
# Cada linha do arquivo representa uma linha da matriz, e as matrizes são sempre quadradas (a quantidade de linhas é a mesma da de colunas).
# A seguir é dado um exemplo de conteúdo de um arquivo csv contendo uma matriz de 4x4:

# 1,2,3,4
# 5,6,7,8
# 9,10,11,12
# 13,14,15,16

# Baseado nisso, responda o que o programa a seguir faz:

# import csv 

# arq = open("c:/users/particular/desktop/matriz.csv", "r")
# csv_reader = csv.reader(arq, delimiter = ',')
# i = 0
# for linha in csv_reader:
#     print(linha[i])
#     i = i + 1
# arq.close()

# Escolha uma opção:
# a. Imprime linha sim, linha não (de forma intercalada) da matriz.
# b. Imprime os valores da diagonal principal da matriz no arquivo.  Resposta
# c. Imprime o primeiro valor de cada linha da matriz no arquivo.
# d. Imprime cada uma das linhas da matriz no arquivo.
# e. Imprime a soma das linhas das matriz no arquivo.

# --------------------
# Questão 04
# Considere um arquivo chamado exemplo.csv que possui o seguinte conteúdo:

# Nome;Idade;Salário
# Maria Silva;45;8500,85
# José Oliveira;30;5500,4
# Marcos Santos;35;8000


# Ao executar o programa a seguir, o que é impresso na tela?
# import csv

# arq = open("c:/users/particular/desktop/exemplo.csv", "r")
# csv_reader = csv.reader(arq, delimiter= ';')
# for linha in csv_reader:
#     print(linha[1])
#     next(csv_reader)
# arq.close()

# Escolha uma opção:
# a. 45
# 30
# 35
# b. Nome
# Maria Silva
# José Oliveira
# Marcos Santos
# c. Idade
# 30     Resposta
# d. 30
# e. Idade
# 45
# 30
# 35