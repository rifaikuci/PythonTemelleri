 # ****************** Set ****************

 # listelere benzerdir.
 # en önemli özelliği indexsiz ve sırasız elemanlardan oluşur
 # veri tekrarı söz konusu olamaz. tüm elemanlar eşsizdir.
 # bu veri yapısı performanslı bir data sağlar.
 # sytanx - > mySet = {1,2,3}

studentsSet = {"Rifai", "Betül", "Ahmet", "Hadi", "Gülhan", "Muta"}
studentsSet2 = ("Mehmet")
 # sytanx olarak böylede kullanılrı.


print(type(studentsSet))
print(type(studentsSet2))


print(studentsSet) # yazdırabileceği en hızlı nasılsa öyle yazdırır. elemanları sırası yoktur.

print("Rifai" in studentsSet)  # öğrenciler setinde Rifai değeri varmı diye kontrol eder.

studentsSet.add("Mehmet")
print(studentsSet)

#birden fazla veri eklenmek isterse update komutu kullanılır.

studentsSet.update(["Murat","Gülsüm", "Esra", "Merve", "Emir"])
studentsSet.remove("Murat")
#studentsSet.remove("Murat") Murat ismini tekrar aramaya çalışacak fakat bulamayacağı için hata döndürecek eğer hata
# döndürmesini istemiyorsak discard fonksiyonu kullanılır.
studentsSet.discard("Murat") # Murat fonksiyonunu studentsSet içinde arıyor
 # fakat bulamıyor discard kullandığımız için hatada döndürmüyor
print(studentsSet)

