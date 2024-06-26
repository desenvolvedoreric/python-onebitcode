from os.path import dirname

archive = f"{dirname(__file__)}/textos.csv"

movies = []

with open(archive, encoding="utf-8") as file:
    for row in file:
        movie, gender, year = row.rstrip().split(",")
        movies.append(f"{movie} > {gender} > {year}") 

for movie in sorted(movies):
    print(movie)