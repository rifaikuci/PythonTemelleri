import pandas as pd
import  numpy as np

data = np.array(["Rifai", "Hifa", "Ahmet","Mahmu"])

#s = pd.Series(data) #boyle tanımlandığında pandas kutuphanesi bizim için arka planda indexliyor
# eğer index'i kendimizde tanımlayabiliriz fakat bu sefer dizi ile aynı olmadığında hata döndürecektir.
# aşağıdaki gibi index 7'den başlatılacaktır.P

s = pd.Series(data,index=[1,5,7,8])


#print(s[5]) # burada indeximize göre 5 olan Hifa getierecektir.

data2 = {"Matemakk" : 10 , "Fizik" : 20 , "Beden" : 100}
# s2= pd.Series(data2) # sözlük türünde tanımladığımız data2 değişkeni sayilari index olarak alıyor.

s2 = pd.Series(data2,index=["Fizik","Matemakk","Beden"]) # eger index tanımlarken string kullanırsak sözlükte tanımlanan gibi
# index ile tanımlanan stringler birebir aynı olmak zorundadır. diğer türlü NaN hatası dönmektedir.
print(s2)
print(s2[0]) # index 0 olan Fizik olduğu için 20 fiziğe karşılık gelen 20 döndürecektir.
print(s2["Matemakk"]) # Matemakk karşılık değeri 10 olduğun için 10 değeri döndürecektir.

s3 = pd.Series(5,index=[1,2,3,4,5,6]) # 5 değeri olan index'te belirtilen kadar deeğer oluşturur.
#s3 = pd.Series(5) # 5 değeri olan index tanımlanmazsa 1 tane değişken oluşur..

print(s3)





