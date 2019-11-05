import pandas as pd

notlar = pd.read_csv("grades.csv")
notlar.columns = ["isim","soyisim","SSN","test1","test2","test3","test4",
                  "final","sonuc"]


#print(notlar)
print(notlar.loc[:5,"isim"]) # ilk indexten başlar sona kadar  isim yazdırır.
# : -> 2 nokta en baştan başla anlamına gelir.

print(notlar.loc[:,"isim":"test4"]) # burada olan ise tüm listeyi al isim'den test4'de kadar yazdır.
# pandas kütüphanesi diğerlerinden farklı olarak dizinin sağındakini de dahil ede. yukarıda da görüldüğü gibi

print(notlar.loc[:5,["isim","soyisim","sonuc"]]) # sadece yazdırmak istediğimiz sütunları virgül(,) ile ayrılır.
print(notlar.loc[:, : "test2"]) # test2 dahil olmak üzere test2'te kadar sütunlar yazdırılır.
print(notlar.loc[::-1,"isim"]) # tersten yazdırılır.


