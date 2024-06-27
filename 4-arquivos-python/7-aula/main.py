from os.path import dirname

archive = f"{dirname(__file__)}/textos.csv"

movies = []

with open(archive, encoding="utf-8") as file:
    for line in file:
        name, gender, year = line.rstrip().split(",")
        movie = {}
        movie["name"] = name
        movie["gender"] = gender
        movie["year"] = year
        movies.append(movie)

def get_movie_name(movie):
    return movie["name"]

def get_movie_gender(movie):
    return movie["gender"]

for movie in sorted(movies, key=get_movie_name):
    print(f"{movie['name']} - {movie['gender']} - {movie['year']}")