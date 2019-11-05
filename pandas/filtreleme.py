

import  pandas as pd

films = pd.read_csv("imdb-1000.csv")

 # prinnt(films.title ile print (films["title"]) ile aynı işlevi görür.
# print(films.columns)
# print(films.head())
# print(films.title.tail())
# print(films[["title","star_rating"]].head())
# print(films[:9][["title","star_rating"]])
# print(films[films["star_rating"]>=9.0][["title","star_rating"]])
# print(films[(films["star_rating"]<9.0) &(films["star_rating"]>8.7)][["title","star_rating"]]) # and komutu
# pandasta or | komutuda bu şekilde yapılabilir
#anlaşılıyor .
#print(films)


print(films.query('(star_rating>9.0)| (star_rating<8.7 & star_rating>8.4)')[['title',"star_rating"]])