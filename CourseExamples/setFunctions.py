# -*- coding: utf-8 -*-

setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

# union
print(setA | setB)
print(setA.union(setB))
print(setB.union(setA))

# intersection
print(setA & setB)
print(setA.intersection(setB))
print(setB.intersection(setA))

# difference
print(setA - setB)
print(setA.difference(setB))
print(setB.difference(setA))

# symmetric difference
print(setA - setB)
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))
