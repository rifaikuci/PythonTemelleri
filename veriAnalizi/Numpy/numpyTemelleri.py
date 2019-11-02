import  numpy


a = numpy.arange(15) #0,dan 15'e kadar bir liste oluşturur.
# fakat listeden farkı ayrac olarak boşluk kullanılor.

a = a.reshape(3,5) # yukarıda oluşan a degerini 3 satır 5 sütuna dönüştürür.



print(a)

print(a.shape ) # a degeri (3,5)

print(type(a)) # a'nın tipini yazdırır.

print("A listesinin boyutu  = " + str(a.ndim))

b = numpy.arange(10)

print(b.shape)  # dizini boyutunu döndürür. (10,) -> 10 sütun 1 satır.

print(b.ndim) # tek boyutlu bir dizi 