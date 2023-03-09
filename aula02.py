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

opcao = input("Forma de pagamento [c|d|b|o]:")

if(opcao == 'c'):
    print("Pagamento no crédito sem desconto.")
elif(opcao == 'd'):
    print("Pagamento no débito com 3% de desconto.")
elif(opcao == 'b'):
    print("Pagamento no boleto com 5% de desconto.")
elif(opcao == 'o'):
    print("PAgamento em dinheiro com 10% de desconto.")
else:
    print("Opção '{}' não cadastrada".format(opcao))