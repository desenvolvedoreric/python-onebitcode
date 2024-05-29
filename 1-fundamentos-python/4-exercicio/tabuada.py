## Tabuada
# Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário

print("=== Descubra os valores da sua tabuada ===")

baseNumber = int(input("Insira o número da tabuada que deseja: "))
startNumber = int(input("Insira o número de começo da tabuada: "))
finishNumber = int(input("Insira o número final da tabuada: "))
count = startNumber

while count <= finishNumber:
  if(count >= startNumber): 
    print(f"{baseNumber} x {count} = {baseNumber * count}") 
  
  count += 1
  
print("=== Fim da tabuada! ===")