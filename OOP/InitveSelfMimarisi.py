

class Matematik :

    def __init__(self,sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2

    def topla(self ):
        return self.sayi1+self.sayi2

    def cikarma(self ):
        return self.sayi1-self.sayi2

    def carpma(self ):
        return self.sayi1*self.sayi2

    def bolme(self ):
        return self.sayi1//self.sayi2



matematik = Matematik(-7,15)

# yukarıda 3 parametre gönderilmesine rağmen biz sadece 2 parametre gönderdik çünkü self parametresi default olarak gelir
# ve Matematik classını referans alması sağlanmıştır.

print(matematik.topla())
print(matematik.cikarma())
print(matematik.carpma())
print(matematik.bolme())