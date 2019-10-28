
import  json

data =' {"adSoyad" : "Rifai", "soyad" : "Kuci", "age" : 15}'

y = json.loads(data)

print(y) # hepsini yazdirir.
print(y["adSoyad"]) # hangi anahtari çağırırsak value döndürür.


customer = {
    "rifai" : "kuci",
    "betul" : "deneme",
    "Oldu " : "Galiba"
}

customerJson = json.dumps(customer) # yukarida olusturan sozlugu json formatina donusturur.
customerJson = json.loads(customerJson) # json olarak donusturur.

print(customerJson["betul"])