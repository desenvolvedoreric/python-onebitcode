import csv
from os.path import dirname

archive = f"{dirname(__file__)}/movies.csv"

name_movie = input("Qual o nome do filme = ")
gender_movie = input("Qual o gênero do filme = ")
year_movie = int(input("Qual o ano do filme = "))

with open(archive, 'a', encoding='utf-8') as file: 
  writer = csv.writer(file, lineterminator='\n')
  writer.writerow([name_movie, gender_movie, year_movie])