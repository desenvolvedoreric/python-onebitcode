from os.path import dirname

archive = f"{dirname(__file__)}/textos.txt"

with open(archive, "r", encoding="utf-8") as file:
    for line in file:
      print(f"Olá {line.rstrip()}")