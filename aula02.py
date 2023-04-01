# resposta = int(input("Qual a resposta para tudo?\nR.: "))

# if resposta != 42:
#     print("Errou, tente novamente!")
 
#---------------------------

# idade = int(input("Digite sua idade: "))
# if idade >= 18:
#     print("Pode dirigir no Brasil...")
# if idade < 18:
#     print("Não pode dirigir no Brasil...")
# if idade > 15:
#     print("Pode dirigir nos EUA...")
# if idade >= 16 and idade < 21:
#     print("Pode dirigir, mas não comprar álcool nos EUA...")

#---------------------------

# idade = int(input("Digite sua idade: "))
# if (idade > 16 or idade >= 70):
#     print("Pode votar!")
#     print("Já fez seu título de eleitor?")
# if (idade >= 18 and idade < 70):
#     print("Na sua idade, o voto é obrigatório.")
# if (idade < 16):
#     print("Você ainda não pode votar!")

#---------------------------

# idade = int(input("Digite sua idade: "))
# if (idade >= 16):
#     print("Você pode votar!")
# else:
#     print("Você ainda não pode votar!")

#---------------------------

# a = int(input("Digite o valor de 'A': "))
# b = int(input("Digite o valor de 'B': "))

# if(a > b):
#     print("A é maior do que B ({} > {})". format(a,b))
# elif(a < b):
#     print("B é maior do que A ({} > {})". format(b,a))
# else:
#     print("A e B são iguais!")

#----------------------------

# opcao = input("Forma de pagamento [c|d|b|o]:")

# if(opcao == 'c'):
#     print("Pagamento no crédito sem desconto.")
# elif(opcao == 'd'):
#     print("Pagamento no débito com 3% de desconto.")
# elif(opcao == 'b'):
#     print("Pagamento no boleto com 5% de desconto.")
# elif(opcao == 'o'):
#     print("PAgamento em dinheiro com 10% de desconto.")
# else:
#     print("Opção '{}' não cadastrada".format(opcao))

#----------------------------

# idade = int(input("Digite sua idade: "))
# if (idade >= 16):
#     print("Você já pode votar se tiver título de eleitor.")
#     if (idade >= 18 and idade <= 70):
#         print("Se você é alfabetizado, seu voto é obrigatório!")
#     else:
#         print("Seu voto é facultativo.")
# else:
#     print("Você ainda não pode votar...")

#----------------------------
#Estruturas de repetição FOR
# for i in range(6):
#     print(i)

#-----------------
# palavra = "Python"
# n = len(palavra) #a função 'len' mede o tamanho/cumprimento
# for i in range(n):
#     print(i)

#---------------------
#imprimir a palavra o numero de vezes correspondentes às letras que tem nela
# palavra = "Python"
# for i in range(len(palavra)):
#     print(palavra)


#--------------------
# palavra = "Python"
# for letra in palavra:
#     print(letra)

#--------------------
#Estrutura de repetição WHILE
# n = int(input("Digite um número inteiro: "))
# while (n > 0):
#     print(0)
#     n -= 1
# print("Tempo esgotato!")

#--------------------
#Forçando a saída de um laço
# while(True):
#     letra = input("Digite uma letra diferente de 'q': ")
#     if(letra == 'q'):
#         break
#     print("Você digitou a letra 'q'!")


# cond = True
# while(cond):
#     opcao = input("Digite 'sair' para terminar o laço: ")
#     if opcao == 'sair':
#         cond = False
#     else:
#         print("Ainda no laço...")

# -----------------------------

#Questão 01
# Associe o que cada código abaixo imprime após execução (código separado por cores pra facilitar a visualização)

# i = 0
# while i <= 10:
#     print(i)
#     i += 1

# for num in range(10):
#     if (num%2 == 0):
#         print(num)

# n = 2
# for i in range(10):
#     produto = n*i
#     print(produto)

# for i in range(10):
#     print(i)

# -------------------------

# Questão 02
# Assinale correto ou incorreto. Considere o código abaixo e assinale o que cada conjunto de variáveis imprime 
# (cada conjunto separado por uma cor diferente).

# if(aparelho == 'tv'):
#     if(marca == 'sony'):
#         if(tamanho == 48):

#             print('Equipamento:' aparelho, marca, tamanho)

# else: 

#     tamanho = 50

# elif(marca == 'samsung'):

#     print('Equipamento:' aparelho, marca, tamanho)

# else:

#     print('Equipamento:' aparelho, marca, tamanho)

# ------------------------

# Questão 03
# Assinale "TRUE" ou "FALSE" abaixo, de acordo com a saída esperada do interpretador Python.

# carro = 'honda'
# not (carro == 'honda'  or  carro == 'toyota')

# carro = 'honda'
# not (carro == 'honda'  and  carro == 'toyota')

# carro = 'honda'
# (carro == 'honda'  and  carro == 'toyota')

# carro = 'honda'
# (carro == 'honda'  or  carro == 'toyota')

# carro = 'honda'
# cor = 'prata'
# (carro == 'honda'  or  carro == 'toyota') and (cor == 'prata')

# ---------------------------
# Questão 04
# Considere os comandos abaixo e responda o que imprime (múltipla escolha):

# idade = int(input("Digite sua idade: "))

# if idade >= 18:
#         print("Pode dirigir no Brasil...")

# if idade < 18:

#         print("Não pode dirigir no Brasil!")

# if idade > 15:

#         print("Pode dirigir nos EUA...")

# if idade >= 16 and idade < 21:

#         print("Pode dirigir, mas não comprar álcool nos EUA")

# -----------------------------
# Questão 05
# contador_pares = 0
# contador_impares = 0

# for i in range(34):
#     entrada = input('Digite um numero: ')

#     numero = int(entrada)

#     if numero % 2 == 0:
#         contador_pares += 1
#     else:
#         contador_impares += 1

# print('Quantidade pares:', contador_pares)
# print('Quantidade impares:', contador_impares)