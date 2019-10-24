

num1 = int(input("num1 : "))
num2 = int(input("num2 : "))
num3 = int(input("num3 : "))

print("Max Number {}".format(max(num1,num2,num3)))

if(num1>num2 and num1>num3):
    print("Max num : {}".format(num1))
elif(num2>num1 and num2>num3):
    print("Max num : {}".format(num2))
elif (num3 > num1 and num3 > num2):
    print("Max num : {}".format(num3))


