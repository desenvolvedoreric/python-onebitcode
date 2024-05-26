movie = {
  "name": "Harry Potter",
  "author": "J. K. Rowling",
  "gender": ["Aventura", "Fantasia"]
}

# Adicionar nova chave
movie["year"] = 1998
print(movie)

# Remover Chave
movie.pop("year")
print(movie)

# Buscando valor
author = movie.get("author")
print(author)

# Pegando chaves do dicionario
print(movie.keys());

# Pegando valores do dicionario
print(movie.values());