## Advinhe o Número
# Escreva um programa em Python que gera um número aleatório para que o usuário tente acertar o número. Algumas sugestões para o programa:

import random

randomNumber = random.randint(0, 100)

def options(): 
  print("Escolha uma opção abaixo: ")
  
  panel = """
  1 - Adivinhar número
  2 - Sair
  """
  
  print(panel)
  choise = input("> ")
  
  match choise: 
    case "1":
      print("Qual é o seu chute de 0 a 100?")
      numberSelectedByUser = int(input("> "))
      isCorrectRandomNumber(numberSelectedByUser)
    case "2":
      print("Finalizando programa...")
    case _:
      print("Ops...Opção inválida!")

def isCorrectRandomNumber(numberSelectedByUser):
  if numberSelectedByUser == randomNumber: 
    print(f"Parabéns! Você acertou, o número é: {randomNumber}")
  
  elif numberSelectedByUser > randomNumber:
    print(f"O número {numberSelectedByUser} é maior")
    options()
  else:
    print(f"O número {numberSelectedByUser} é menor")
    options()
    
options()