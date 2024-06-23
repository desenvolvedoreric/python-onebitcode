from os.path import dirname

def read_file_with_limit(archive, limit):
  archive = f"{dirname(__file__)}/{archive}.txt"
  count = 0
  
  with open(archive, 'r', encoding="utf-8") as file:
    for line in file:
      if count == int(limit):
        print("Fim...")
        break
      
      print(line.rstrip())
      count += 1


read_file_with_limit("textos", 3)