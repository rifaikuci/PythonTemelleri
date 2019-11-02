
import pandas
#
firstString = "RifAi KucI"
secondString = "rifai kuci"


# upper string harlerinin büyütülmesini sağlar.

if(firstString.upper() == secondString.upper()):
      print("Kelimeler Eşit")

else:
     print("Kelimeler Eşit Değil")



# Substring Özellikleri

message = "Merhaba Dünya"
#
# print(message[4]) #index döndürür
print(message[4:]) # 4.karakterden itibaren yazdır
# print(message[:4]) # 4.karaktere itibaren yazdır
# print(message[4:8]) # 4.karakterden 6.karaktere kadar yazdır



# Strin Uzunluğu

message ="Rifai Kuçi"

print("message length: ",len(message))



print ("Büyük Harfler Yazdırma ", message.upper())
print ("Küçük Harfler Yazdırma ", message.lower())


# Replace komutu

newMessage = message.replace("a","e")

print(newMessage)


# Strip,split Fonksiyonu
# Strip fonksiyonu baştaki ve sondaki boşlukları silmeye yarar
#split fonksiyonu ise ne ile istenirse diziye çevirmeye yarar.

deneme  = "         Rifai Kuçi 35 engaged     "
deneme=deneme.strip()
deneme=deneme.split(" ")
print(deneme)

# degistirme

x = 10
y = 20

x,y = y, x
print(x, y )







