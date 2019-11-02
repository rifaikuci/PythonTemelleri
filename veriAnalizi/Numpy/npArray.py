import  numpy as np


a = np.array([1,3,5,7,9,11]) # numpy array gönderirken
# liste şeklinde gönderilmesi gerekmektedir.

a = a.reshape(2,3)
print(type(a))

print(a.ndim)
print(a)

b = np.array([[1,2,3],[2,4,7],[7,9,20]])
print(b.ndim)
print(b.shape)
print(b)