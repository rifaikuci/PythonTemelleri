

#map işlemi
from functools import reduce

sayi = [1,2,3,4,5]
sayiKaresi= list(map(lambda x:x*x , sayi))

print(sayiKaresi)


#filter işlemi


sayifilte = list(filter(lambda  x : x>2 , sayi))
print(sayifilte)

#reduce işlemleri

faktorIslemleri = reduce( lambda  x,y : x*y, sayi )

print(faktorIslemleri)