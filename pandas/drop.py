import pandas as pd

films = pd.read_csv("imdb-1000.csv")

print(films.columns)

#eğer axis 1 ise sütundan bir şey silmek istediğimizi anlar ama eğer axis 0 ise satırdan bir şey sileceğimizi anlamına gelir.
films = films.drop("content_rating", axis=1)
films = films.drop("actors_list", axis=1)

films = films.drop(2,axis=0) #2.index silinmesini sağlar, index 0'dan başlar


rowsToDrop = [0,1,4,7,8,9,15]

films = films.drop(rowsToDrop,axis=0)
print(films)
