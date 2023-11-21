# -*- coding: utf-8 -*-

number1 = int(input("First number: "))
number2 = int(input("Second number: "))
number3 = int(input("Third number: "))

if (number1>=number2) and (number1>=number3):
    greatest = number1
    
elif (number2>=number1) and (number2>=number3):
    greatest = number2
else:
    greatest = number3
    
print("Greatest number is: " + str(greatest))