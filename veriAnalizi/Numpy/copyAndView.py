
import numpy as np

a = np.arange(10)
print(a)

b = a
print(b)

b[0] =100
print(a) # fakat biz sadece b[0] değerini değiştirmemize rağmen a daki değeri de değiştirdi
# çünkü a değerini b'ye gönderirken referans kopyalandı değerleer değil
print(b)

c = a.copy()
c[0] = 14
print(c)
print(a)


d = a.view()
print("*********")

print(a)
print(d)
# degeri değiştiriken ikisini de değiştirilir. fakat shape konusunda iyi işler görebilir.

d [0] = 250
print(a)
print(d)

d.shape = 2,5

print(a)
print(d)

a[0]= 123
print(a)
print(d)