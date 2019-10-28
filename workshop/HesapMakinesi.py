

def topla(sayi1,sayi2):
    return sayi1+sayi2


def cikarma(sayi1,sayi2):
    return sayi1-sayi2


def carpma(sayi1,sayi2):
    return sayi1*sayi2

def bolme(sayi1,sayi2):
    return sayi1//sayi2

print("Seçimleriniz " )
print("1- Toplama " )
print("2- Cikarma " )
print("3- Carpma " )
print("4- Bolme " ,end="\n\n\n")

opsiyon = int(input("Secimizi Yapiniz"))

sayi1= int(input("Sayi 1 giriniz : "))
sayi2= int(input("Sayi 2 giriniz : "))


if(opsiyon == 1):
    print(int(topla(sayi1,sayi2)))

elif(opsiyon == 2 ):
    print(int(cikarma(sayi1,sayi2)))

elif(opsiyon == 3 ):
    print(int(carpma(sayi1,sayi2)))

elif(opsiyon == 4 ):
    print(int(bolme(sayi1,sayi2)))

else:
    print("Geçersiz Secim ")