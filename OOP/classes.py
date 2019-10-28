

class Matematik :


    def topla(self ,sayi1,sayi2):
        return sayi1+sayi2

    def cikarma(self ,sayi1,sayi2):
        return sayi1-sayi2

    def carpma(self ,sayi1,sayi2):
        return sayi1*sayi2

    def bolme(self ,sayi1,sayi2):
        return sayi1//sayi2



matematik = Matematik()

# yukarıda 3 parametre gönderilmesine rağmen biz sadece 2 parametre gönderdik çünkü self parametresi default olarak gelir
# ve Matematik classını referans alması sağlanmıştır.

print(matematik.cikarma(4,15))