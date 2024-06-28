import csv
from os.path import dirname

archive = f"{dirname(__file__)}/textos.csv"

movies = []

with open(archive, "r", encoding="utf-8") as file:
    datas = csv.DictReader(file)
    print(datas)
    for movie in datas:
        movies.append(f"{movie['name']} - {movie['gender']} - {movie['year']}")

for movie in movies:
    print(movie)