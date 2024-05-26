## Aumento salário funcionário
# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
# salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
# 15%.

salary = float(input("Olá funcionário! Qual é o valor do seu salário? "))

if salary > 1250: 
  increase = (10 / 100) * salary
  newSalary = salary + increase
  print(f"O seu aumento de salário é R$ {increase:.2f}.\nTotal bruto será de: R${newSalary:.2f}.")
else: 
  increase = (15 / 100) * salary
  newSalary = salary + increase
  print(f"O seu aumento de salário é R$ {increase:.2f}.\nTotal bruto será de: R${newSalary:.2f}.")