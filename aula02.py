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

idade = int(input("Digite sua idade: "))
if (idade >= 16):
    print("Você pode votar!")
else:
    print("Você ainda não pode votar!")