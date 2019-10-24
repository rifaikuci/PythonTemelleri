#********** Diziler Referans Tiptir . *****

# Liste tanımlama  sytax'ı

# myList = [] # empty list
#
# myList2 =  [1,"Deneme", 0.60]
#
# print(myList2.index(0.60))

sehirler = ["Rifai" ,"Hifa", "Betül", "Ahmet","Betül"]

sehirler.append("Mehmet")
sehirler.remove("Rifai")
#
denemeList = (("rİFAİ","kUÇİ"))

print(sehirler.count("Betül")) # listede kaç tane olduğunu döndürür.
print(sehirler.pop(0)) # sehilerden 0.elemanı çıkar
sehirler.insert(0,"Mardin") # 0. elemana Mardini ekle
sehirler.reverse()
print(sehirler)

sehirler3 = sehirler.copy()

sehirler3.append("Kırşehir")
sehirler.extend(sehirler3) #sehirler3'e sehirlere eklemesi yapılır.
sehirler.sort() # sıralamayı yapar
sehirler.reverse()  #ters çevirme işlemini yapar
print(sehirler)

#sehirler.clear() -> sehirler listesinin tamamının silinmesine neden olur

#sehirler.count("Mardin") -> sehirler listesinde kaç tane mardin olduğunu döndürür.