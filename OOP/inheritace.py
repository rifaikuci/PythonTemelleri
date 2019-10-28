


class Person:
    def __init__(self,firstName, lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age


class Work(Person):

    def __init__(self,salary):
        self.salary=salary


class Customers(Work):
    def __init__(self,creditCard):
        self.creditCard = creditCard
        

deneme = Customers("dssdsdsd")


print(deneme.lastName)
