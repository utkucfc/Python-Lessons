# -*- coding: utf-8 -*-

tuple1 = ()
list1 = []

print(type(tuple1))
print(type(list1))

tuple2 = (2,4,6,"Portland",(2,3,4))
list2 = [2,4,6,"Portland",[3,4,5]]

print(tuple2)
print(list2)
print(len(tuple2))
print(len(list2))

list2[0] = 6
# tuple2[0] = 6 ####TUPLE IS READONLY

tupleValue = ("Utku",)
print(type(tupleValue))
print(tupleValue)


print(tuple2[1:2])
print(list2[1:2])

print(tuple2[-2])
print(list2[-2])