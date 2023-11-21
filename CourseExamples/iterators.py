# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:02:16 2023

@author: Admin
"""

cities = ["Ankara","Istanbul","Berlin","New York"]

myIterator = iter(cities)

print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

# print(next(myIterator)) #StopIteration error, out of range
print("**************")
for city in cities:
    print(city)