

 # a append acilan dosyaya veri ekleemesi yapilir. append'den gelir
 # w dosya yazma islemi icin acilir.
 # r dosya okuma islemi icin kullanilir. default olarak kullanilir.
 # x dosya kurma islemimi yapar
f = open("musteriler.txt", "r")

#print(f.read()) #musteriler.txt'deki yazilari konsola yazdirdi.

print("********************************************")

#print(f.read(7)) #musteriler.txt'deki ilk kaç karakter alınmak istenirse karakter sayısı paranteze yazılır.

#print(f.readline()) # readline ise satır satır okunmasını sağlıyor.
#print(f.readline()) # en son nerede kaldıysa devam etmektedir.
dizi = []

for i in f :
    i=i.replace("\n", "")
    dizi.append(i)

f.close() # dosya işimiz bittikten sonra kapanma işlemi için
print(dizi)
