from os.path import dirname

archive = f"{dirname(__file__)}/textos.csv"

with open(archive, "r", encoding="utf-8") as file:
  for row in file:
    movie, gender, year = row.rstrip().split(",")
    print(f"Filme: {movie} > Gênero: {gender} > Ano: {year}")