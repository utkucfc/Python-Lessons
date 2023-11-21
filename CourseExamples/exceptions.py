# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 16:16:53 2023

@author: Admin
"""

try:
    number1 = int(input("Enter a number. "))
except ValueError:
    print("Type error. Please enter an integer")
except ZeroDivisionError:
    print("Can not divide zero")
except (IndexError,ArithmeticError):#Example
    print("USAGE: 2 error types within same brackets")
except:
    print("Unhandled exception")
    
print("END")
