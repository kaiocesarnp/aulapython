# resposta = int(input("Qual a resposta para tudo?\nR.: "))

# if resposta != 42:
#     print("Errou, tente novamente!")

#---------------------------

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Pode dirigir no Brasil...")
if idade < 18:
    print("Não pode dirigir no Brasil...")
if idade > 15:
    print("Pode dirigir nos EUA...")
if idade >= 16 and idade < 21:
    print("Pode dirigir, mas não comprar álcool nos EUA...")