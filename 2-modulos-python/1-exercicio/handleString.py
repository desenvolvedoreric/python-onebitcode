## Módulo de strings
# Escreva um módulo em python para tratar algumas strings e que possua as seguintes funcionalidades:
# 1. Inverter uma string de trás pra frente.
# 2. Retornar apenas letras com índice par.
# 3. Retornar apenas letras com índice ímpar.

def reverseString(string): 
  return string[::-1]

def lettersEven(string): 
  even = []
  
  for index in range(len(string)): 
    if(index % 2 == 0): 
      even.append({
        "indice": index,
        "Letra": string[index] 
      })
  
  return even

def lettersOdd(string): 
  odd = []
  
  for index in range(len(string)): 
    if(index % 2 != 0): 
      odd.append({
        "indice": index,
        "Letra": string[index] 
      })
  
  return odd