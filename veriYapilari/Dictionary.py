

#******************************* Dictionary ************************
# aynı set gibi verileri sırasız tutar.
# günlük hayattaki sözlüğe benzetebiliriz.
# birinci tanımlanan key ikinci tanımlanan ise value
myDict = {
    "key"  : "value",
    "book" : "kitap",
    "notebook" : "defter",
    "bag" : "canta",
    1 : "one",

}

myDict2 = dict(masa = "Rifai", deneme = "TRY again")
print(type(myDict))
myDict["bag"] ="valiz"
print(myDict.get("bag"))
print(myDict["notebook"])

#silme işlemi için del kullanılır

del(myDict["key"])

# yeni bir eleman eklemek için

myDict["Kulaklık"] ="heared"

print(myDict)
print(myDict2)