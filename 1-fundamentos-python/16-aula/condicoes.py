print("=== CARTEIRA DE MOTORISTA ===")
name = input("Digite o seu nome cidadão: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
  print(f"Olá {name}, você está apto a tirar CNH")
else:
  print(f"Olá {name}, você não está apto a tirar CNH")