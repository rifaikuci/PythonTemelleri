

ogrenciler=["Rifai Kuçi", "Betül Şafak","Hadi Kuçi", "Edibe Kuçi", "Hifa Hatun", "Mehmet Alaca", "Güntekin Kurtuluş"
            ,"Gülhan Şafak", "Şehabettin Şafak"
            ]

f = open("aileFertleri.txt","a")

for i in ogrenciler:
    f.write(i)
    f.write("\n")


f.close()