
import pandas as pd

films = pd.read_csv("imdb-1000.csv")

print(films.columns)
print(films.head())
print(films.star_rating.mean()) # star_rating verilerdeki ortalamayı almasını sağlar.
print(films.groupby('genre').star_rating.mean()) # türüne göre ortalaması
print(films.groupby('genre').count()['title']) # türüne göre grupladık