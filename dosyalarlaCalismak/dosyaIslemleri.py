import os

f = open("Ogrenciler.txt","a") # dosya kurduk

#f.write("Rifai\n")
f.write("Dneme")
f.close()


if(os.path.exists("Ogrenciler.txt")==False): # dosya olup olmadığına bakılır.
    print("Ogrenciler dosyasi var")
else:
    os.remove("Ogrenciler.txt") # silme işlemlerini yapar


os.rmdir("deneme")