## Cálculo da Distância
# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
# 0,35 para viagens mais longas.

distance = float(input("Olá passageiro, informe quantos km vamos percorrer hoje: "))

if distance <= 200:
  priceByDistance = 0.50
  print(f"O valor cobrado pela passagem será de: {distance * priceByDistance}")
else:
  priceByDistance = 0.35
  print(f"O valor cobrado pela passagem será de: {distance * priceByDistance}")
