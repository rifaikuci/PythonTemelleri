
# ******************** Tuple***************

# Listelere benzerdir
# Tek farkı listelerde eleman değiştirebilirken tupleda eleman değiştirme işlemi yapılamaz

# bu veri performanslı bir yapı sağlar
# myTuple = () -> syntax

tupleListe = (2,5, "Adana",(2,7,8),[2,1,7])

Liste =[2,5,"Adana",[2,1,7],(2,7,8)]

# tuple eleman olarak liste ve tuple değerleri alabilir
# liste eleman olarak liste ve tuple değerleri alabilir


#tupleListe.append("Medine") tuple liste eleman ekleme işlemi yapılamaz

Liste.append("Bursa")


print(len(tupleListe)) # eleman sayısını döndürür
print(len(Liste)) #  eleman sayısını döndürür

print(type(tupleListe)) # tipini döndürür.
print(type(Liste)) # tipini döndürür.

print(Liste[-2])
print(tupleListe[-1]) # tersten yazdırma işlemi

print(tupleListe[1:2]) # 1'den 3 e kadar elemanları yazdırır tuple olduğunu göstermek için sonuna , ekler
print(Liste[1:2]) # 1'den 2. elemana kadar elemanları yazdırır.