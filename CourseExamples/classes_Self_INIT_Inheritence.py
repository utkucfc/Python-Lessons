# -*- coding: utf-8 -*-
class matematik:
    def __init__(self, input1, input2, operation):
        self.input1 = input1
        self.input2 = input2
        self.operation = operation
        if self.operation == 1:
            matematik.topla(self)
        elif self.operation == 2:
            matematik.cikar(self)
        elif self.operation == 3:
            matematik.carp(self)
        elif self.operation == 4:
            matematik.bol(self)
    
    
    def topla(self):
        res = self.input1 + self.input2
        print(res)
        
    def cikar(self):
        res = self.input1 - self.input2
        print(res)
        
    def carp(self):
        res = self.input1 * self.input2
        print(res)
        
    def bol(self):
        res = self.input1 / self.input2
        print(res)
        
print("Which operation do you want to do? / Hangi işlemi yapmak istiyorsunuz?")
print("1-Add/Topla")
print("2-Subtract/Çıkart")
print("3-Multiply/Çarp")
print("4-Divide/Böl")

chosen = int(input("Pick/Seç(1-2-3-4): "))
firstNumber = int(input("Enter the first number/İlk sayıyı giriniz: "))
secondNumber = int(input("Enter the second number/İkinci sayıyı giriniz: "))
matematik(firstNumber,secondNumber,chosen)

##################

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
person1 = Person("Utku","CIFCI",25)
print(person1.firstName)
        
class Worker(Person):
    def __init__(self,salary):
        self.salary = salary
class Customer(Person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
      
leonardo = Worker(300)
print(leonardo.salary)

donatello = Customer(1111222233334444)
print(donatello.creditCardNumber)