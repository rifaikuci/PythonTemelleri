


try:
    sayi = int(input("Sayi giriniz..."))
except (ValueError,ZeroDivisionError):
    print("Tip Uyuşmazlığı")

except:
    print("Hata oluştu ")    