

import  numpy as np


sayilar = np.array([0,5,10,15,20,25,30])

print(sayilar[ :: -1]) # tersten sıralama yapmasını sağlar

print(sayilar [0:3]) # ilk 3 elemanı döndürür.
print(sayilar [5]) # 5. elemana döndürür.[0,5,10,15,20,25,30]


sayilar2  = np.array([[0,5,10],[15,20,25]])

print(sayilar2[:,0:1]) # tüm diziler arasında 0.elemanı alın

print(sayilar2[-1 ,:   ])
print(sayilar2[ : ,- 1   ])

print(sayilar2[1][0])