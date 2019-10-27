

Sehirler = ["İstanbul", "Ankara", "Mardin", "İzmir", "Sivas", "Burdur"]


# İstanbul ile ankara yazıldı fakat Mardine geldiğinde döngü kırıldı.
for sehir in Sehirler:

     if(sehir == "Mardin"):
         break
     print(sehir)



#  Mardini gördü fakat yazdırmadı geldiğinde döngü kırıldı.

for sehir in Sehirler:

     if(sehir == "Mardin"):
         continue
     print(sehir)