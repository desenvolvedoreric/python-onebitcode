# Desafio 1: Substituir caractere repetido
# Grave o primeiro caracter, e troque os demais repetidos por $. 
# FIFA 23 --> FI$A 23 = Segundo F trocado por $.

text = "FIFA 23"
char = text[0]
newText = char + text[1:].replace(char, "$")
print(newText)

# Desafio 2: Gerando String:
# Entrada: "abc" "def"
# Saida: "dec" "abf" --> Dois primeiros caracteres foram trocados de string.

str1 = "abc"
str2 = "def"

newStr1 = str2[:2] + str1[2:]
newStr2 = str1[:2] + str2[2:]

print(newStr1)
print(newStr2)