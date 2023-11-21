# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:07:27 2023

@author: Admin
"""

numbers = [1,2,3,4,5]

# numbersSquared = []
# for number in numbers:
#     numbersSquared.append(number**2)


print("Numbers list: " + str(numbers))

#MAP
numbersSquared = list(map(lambda number: number**2,numbers))
print("Squared List: "+ str(numbersSquared))

#FILTER
numbersFiltered = list(filter(lambda number: number>4,numbersSquared))
print("FILTERED 'Squared List'"+ str(numbersFiltered))

#REDUCE
from functools import reduce
numbersfactorial = reduce(lambda x,y:x*y,numbers)
print("Result of the factorial of the numbers in original list: " + str(numbersfactorial))