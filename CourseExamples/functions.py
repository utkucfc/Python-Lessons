# -*- coding: utf-8 -*-

# city = "Ankara"

# print(city.upper())
# print(city.endswith("a"))

def Greatings():
    print("Hello")
    
Greatings()


def Greatings2(name):
    print("Hello " + name)
    
Greatings2("Leonardo")


def Greatings3(name = "Buddy"):
    print("Hello " + name)
    
Greatings3()
Greatings3("Raphael") 
 
    
def Greatings4(name,surName = "Adam"):
    print("Hello " + name + " " + surName)
    
Greatings4("David")



#return functions
def AreaOfRightTriangle(a,b):
    return (a*b)/2

area = AreaOfRightTriangle(2, 3)
print(area)


AreaOfRightTriangle2 = lambda a,b : (a*b)/2
print(AreaOfRightTriangle2(3, 6))


x = AreaOfRightTriangle2
print(x(4,6))


