## Verificar conteúdo da String
# Escreva um programa em Python para verificar se uma string contém apenas um determinado conjunto de caracteres (neste caso, a-z, A-Z e 0-9).

import re

# Ele não identifica espaços.
def hasSpecialCharacters(word):
  rule = re.compile(r"[^a-zA-Z0-9]")
  string = rule.search(word)
  return not bool(string)

print(hasSpecialCharacters("bbbbb77*"))