


sayi = int(input("Bir sayi giriniz"))
sonuc=1

if (sayi < 0):
    print("Sayi negatif olamaz")


elif(sayi==0):
    print("Faktoriyel = 1 ")
else:

    for i in range(1,sayi+1):
       sonuc=sonuc*i

    print(sayi, " faktoriyeli ", sonuc)


