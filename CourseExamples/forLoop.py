# -*- coding: utf-8 -*-

cities = ["Ankara","Berlin","Tokyo","New York","Austin"]
# print(cities[0])
# print(cities[1])
# print(cities[2])
# print(cities[3])
# print(cities[4])

for city in cities:
    if city == "Tokyo":
        continue
    # if city == "Ankara":
    #         break
    print(city[0:3] + " is shortcut for " + city)
    print("****************")
    
#&&
for x in range(2,100,2):
    print(x)
