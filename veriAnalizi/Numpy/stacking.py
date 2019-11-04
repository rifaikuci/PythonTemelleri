

import numpy  as np

a = np.floor(10*np.random.random((2,3)))
b = np.floor(10*np.random.random((2,3)))

print(a)
print(b)

print("\n\n\n********************************************* Dikey Birleştirme ")
c = np.vstack((a,b)) # dikey birleştirme
print(c)
print("\n\n\n********************************************* Yatay Birleştirme ")
d = np.hstack((a,b)) # hatay birleştirme

print(d)
