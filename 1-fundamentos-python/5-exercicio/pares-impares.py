## Lista números pares e ímpares de uma lista
# Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.

def checkEvenOrOdd(*numbers): 
  numbersDefinition = {
    "odd": [],
    "even": []
  }
  
  for number in numbers: 
    if number % 2 == 0:
      numbersDefinition["even"].append(number)
    else: 
      numbersDefinition["odd"].append(number)
  
  return numbersDefinition 

print(checkEvenOrOdd(1, 2, 3))