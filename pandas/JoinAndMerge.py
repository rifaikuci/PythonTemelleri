import  pandas as pd

data1  = {
        'id' : [1,2,3,4],
        'ad' : ["Engin","Rifai","Hifa","Hadi"],
        'soyad' : ["Demirog","Kuci","Hatun","Haydar"]

}

data2 = {
    'id': [1, 3, 4, 7 ],
    'ad': ["Esra", "Ahmet", "Emir", "Eylul"],
    'soyad': ["Hanim", "Kuci", "safak", "safak"]
}

data1Df = pd.DataFrame(data1)
data2Df = pd.DataFrame(data2)
#
# print(data1Df)
# print(data2Df)

print(pd.merge(data1Df,data2Df,on='id',how='inner')) # eşleşen id'leri alır sadece
print(pd.merge(data1Df,data2Df,on='id',how='left')) # ortak olanları zaten alır. ve buna ek olarak solda olanlarıda alır.
print(pd.merge(data1Df,data2Df,on='id',how='right')) # ortak olanları zaten alır. ve buna ek olarak solda olanlarıda alır.


print(pd.concat([data1Df,data2Df])) # data1df data2df ile birleşir
#bizim yaptığımızda tamamen alan adaları aynı olduğunda ek bir sütun acilirdi ad yerine bir tanesi adi
#olsaydı id ad soyad adi olarak 4 sütunumuz olurdu.
print(pd.concat([data1Df,data2Df],axis=1)) # eğer yan yana yazdırmak istersek axis = 1 eklenir
