
import numpy as np

a = np.array([20,30,40,50])
b = np.arange(4) # buradan oluşan array [0,1,2,3]

c = a-b # matrislerde çıkarma işlemi yapılıyor

# yapılırken satır ve sütun sayıları eşit olmalı

d = a+b # toplama işlemi de aynı şekilde

d = b**3 #b'dekilerin küpünü al d'ye aktar.

e = 10* np.sin(a) # sin a değerleri alınıp 10 ile çarpıldı ve e değerine aktarıldı.

f = a*b # a ile b değeri satır satır sütun sütun çarpıldı.

g = a @ b # matris çarpımlarının toplamını verir


f = a.dot(b) # a @ b ile bire bir aynı sonucu verir.

g = np.zeros((2,4)) # 2 ile 4  0 matrisi oluşturur.
h = np.ones((2,4))  # 2 ile 4 birim matrisi oluşturur.

i = np.sum(a) # a dakileri alır toplar
k = np.random.random((2,4)) # 0 1 arasında random değerler oluşturur.

j = np.sqrt(a)

m = np.max(k) # k daki değerlerin en büyüğünü m'ye atar.
n = np.min(k) # k daki değerlerin en küçüğünü n'ye atar.

print(m)
print(n)

