## Conta letras maiúsculas e minúsculas
# Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.

def countUppercaseCharacters(string):
  charsList = [char for char in string if char == char.upper()]  
  return len(charsList)

def countLowercaseCharacters(string):
  charsList = [char for char in string if char == char.lower()]  
  return len(charsList)

uppercaseCount = countUppercaseCharacters("ErIc")
lowercaseCount = countLowercaseCharacters("Eric")

print(uppercaseCount)
print(lowercaseCount)