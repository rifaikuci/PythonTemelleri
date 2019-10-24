
# set union setleri birleştirir. birleşime karşılık gelir.

setA= {1,2,4,7,8,5,3}
setB = {3,4,6,2,7,9}
print("**********************Birleşim****************************" )

print(setA | setB)
print(setA.union(setB))

print("**********************Farkı****************************" )

print(setA - setB)
print(setA.difference(setB))
setF=setA.difference(setB)
print(setF)
setC = setA.union(setB)
print(setC)

# set intersection. setler arasında kesişim olan elemanları döndürür.
print("**********************Kesişim****************************" )

print(setA & setB)
print(setA.intersection(setB))
setD = setA.intersection(setB)
print(setD)



print("**********************Kesişim dışında kalacak elemanlar****************************" )

print(setA ^ setB)
print(setA.symmetric_difference(setB))
setG=setA.symmetric_difference(setB)
print(setG)