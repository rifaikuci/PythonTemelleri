
import pandas as pd

notlar = pd.read_csv("grades.csv")
notlar.columns = ["isim","soyisim","SSN","test1","test2","test3","test4",
                  "final","sonuc"]
diziSayi =[]
for i in range(16):
    diziSayi.append(i+1)

print(diziSayi)

notlar.index = [diziSayi]

print(type(notlar))
print(notlar.head()) # ilk 5'i getirir.
print(notlar.tail()) # son 5' i getirir.

print(notlar)
print(notlar["final"])
print(notlar.loc[2])
print(notlar.iloc[2])

print(notlar[0:10])