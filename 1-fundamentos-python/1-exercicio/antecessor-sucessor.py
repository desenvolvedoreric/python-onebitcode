# Desafio 1: Antecessor e Sucessor
# Lê um número
number = int(input("Digite um número: "))
number_temp = number
# Representa o número antecessor utilizando operadores de atribuição
number -= 1
# Representa o número sucessor utilizando operadores de atribuição
number_temp += 1

print(f"Antecessor: {number} \nSucessor: {number_temp}")