from os.path import dirname

print("Adicione texto em um arquivo de texto.")
text = input("Text: ")

archive = f"{dirname(__file__)}/textos.txt"

with open(archive, 'a') as file:
  file.write(f'{text}\n')