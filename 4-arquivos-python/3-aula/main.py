from os.path import dirname

archive = f"{dirname(__file__)}/textos.txt"

fruits = []

with open(archive, "r", encoding="utf-8") as file:
    for line in file:
      fruits.append(line.rstrip())

for fruit in sorted(fruits):
  print(fruit)