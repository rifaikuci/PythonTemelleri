"""
1 2 3
4 5 6
1 2 3

+
2 3 5
8 7 1
1 4 7

=
3 5 8
12 12 7
2 6 10
"""
# dizi 1
matris1= []
b=1
for i in range(0,3):
    for j in range(0,3):
         sayi1=input(str(i)+  ".inci satir" +  str(j)+ " . inci sutun degeri :" )
         matris1.append(sayi1)

for i in range(0,9):
    print(matris1[i], end="\t")
    if(b%3==0):
        print("\n")
    b+=1


#dizi2
c=1
matris2= []
for i in range(0,3):
    for j in range(0,3):
         sayi1=input(str(i)+  ".inci satir" +  str(j)+ " . inci sutun degeri :" )
         matris2.append(sayi1)

for i in range(0,9):
    print(matris2[i], end="\t")
    if(c%3==0):
        print("\n")
    c+=1


 #dizilerin toplami
a=1
for i in range(0,9):
    print(int(matris1[i])+int(matris2[i]), end="  ")

    if(a%3 == 0 ):
        print("\n")
    a+=1