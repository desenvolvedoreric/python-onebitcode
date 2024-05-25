movies = ["Harry Potter", "Velozes e Furiosos", "Sempre Ao Seu Lado", "Star Wars"]

# Verificar tamanho da lista. 
print(len(movies))

# Retorna o indice do elemento.
print(movies.index("Harry Potter"))

# Adicionar item no fim da lista.
movies.append("Fique Rico ou Morra Tentando")
print(movies)

# Remove o último elemento da lista ou remove um item com seu respectivo indice como parâmetro.
movies.pop() # pop(1)
print(movies)

# Adicionar item em uma determinada posição
movies.insert(0, "O Treinamento dos Hashiras")
print(movies)