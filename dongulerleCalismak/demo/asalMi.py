


sayi  = int ( input("Sayi giriniz "))
asalmi = True

for i in range(2,sayi):
    if (sayi%i) == 0:
        asalmi=False
        break


if(asalmi == True):
    print("Asal Sayi")
else:
    print("Asal sayı değil")
