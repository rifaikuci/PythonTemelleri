

import  numpy as np

a = np.floor(10* np.random.random((3,6))) # floor ile int haline getirirliyor.


print(a)

print(a.shape) # dizi boyutu

print(a.ravel()) # tek boyuta çevirir
#a =a.ravel()  # tek boyuta çevirdi değişken olarak kaydedildi.
print(a.shape)

a = a.reshape (2,9) # boyutu 3,6ya değiştirildi
print(a)

print(a.T) # matrislerde transpozan yandakileri yataya geçirildi. örnek

'''
[2,7,9]                     [2,1]
                            [7,9]
                            [9,8]
[1,9,8]  = > transpoz hali
'''
print(a.reshape(2,-1))