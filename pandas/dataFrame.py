import  pandas as pd

data = [10,20,30,40,50]

df = pd.DataFrame(data) # data frame oluşturulması fakat serieslerden farklı olarak buradan kolonlarda oluşuyorç

#print(df)

# data2 = [["Rifai", 22, "Mardin"],["Hifa",21,"Konya",],["Hadi",48,"istanbul"]] #0.kolon Rifai,Hifa, Hadi, 1. kolon yaşlar , 3.kolon şehirler
#eğer kolonlara kendimiz'de isim verebiliriz.
data2 = [["Rifai", 22, "Mardin"],["Hifa",21,"Konya",],["Hadi",48,"istanbul"]]
df2 =pd.DataFrame(data2,columns=["İsim","Yaş","Şehir"],index=[4,5,6]) # burada hem sütun hemde indexleri tanımladık eğer tanımlamazsak default olarak 0'dan başlar.

# print(df2)

# sozluk olarak dataframe tanımlamak
data3 = { "İsim" :["Riai", "Hifa", "Hadi"],
          "Yaş" : [22,21,48],
          "Şehir" : ["Mardin", "Konya", "istanbul"]

          }

df3 =pd.DataFrame(data3,index=[1,2,3],columns=["İsim","Yaş","Şehir"])
#print(df3["Şehir"]) # şehir objectinin tipini döndürür.

# del df3["Şehir"] # şehir sütununu silme işine yara
#df3.pop("Şehir") # del df3["Şehir"] birebir aynıdır.
print(df3)

print(df3.loc[2])  # bizim verdiğimiz index'e göre arama yaptırır. 2.index'Te hifa bulunuyor.
# sadece hifa'ya ait olan veriler döndürür.

print(df3.iloc[2]) # burada ise normal dizilerdeki gibi 0' ı esas alır. 0. index Rifai 1. index Hifa 2. index Hadi
# olduğu için Hadiye ait olanları döndürür.


# eğer aynı formatta veriler varsa bunları append komutu ile birleştirebilir. biz biliyoruzji df1 df2 ve df3 aynıdır.
df4 = df3.append(df2)
print(df4)


print(df4.head()) # yapılacak büyük projelerde veri sayısı çok aşırı olacaktır.
# bundan dolayı kolay açılması için verileri alırken ilk 5 veriyi almamız gerekebilir bu sayede veriler hakkında bilgimiz olabilecektir.

print(df4.tail())# tail ise veriler sondan 5 almamızı sağlayacaktır.
