import  sys

liste = [1,"Rifai", 0,7, "deneme",6]

for i in liste:
    try:
        print(str(i) + " : Sayisi icin " )
        sonuc = float(1/i)
        print(sonuc)
    except TypeError:
            print(str(i) + " sayisi : Type donusum hatasi ")
    except ZeroDivisionError:
        print(str(i)  + " sayisi : 0'a bolunemez")
    except :
        print(sys.exc_info())

    finally:
        print("try-except'te bittiğinde en son çalışılacak yerlerdir.")