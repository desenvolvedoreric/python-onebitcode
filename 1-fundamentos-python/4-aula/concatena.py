name = input("Qual o nome do jogo?\n")
yearLaunch = int(input("Qual o ano do jogo?\n"))
isExpensive = input("É um jogo caro?\n")
price = float(input("Qual o valor do jogo?\n"))

print("###Dados do Jogo####")
print("====================")
# Alternativa 1
# print("Nome do Jogo:", name)
# print("Ano do Jogo:", yearLaunch)
# print("Preço do Jogo:", gamePrice)
# print("Está incluído no plano?", planIncluded)

# Alternativa 2
# print("Nome do Jogo:", name, "\nAno de lançamento:", yearLaunch,
#       "\nPreço do Jogo:", gamePrice, "\nEstá incluso no serviço?", planIncluded)

# Alternativa 3
print(f"Nome do Jogo: {name} \nAno Lançamento: {yearLaunch} \nPreço do Jogo: {price} \nÉ caro? {isExpensive}")