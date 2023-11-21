# -*- coding: utf-8 -*-

# student1 = "Utku"
# student2 = "George"
# student3 = "Ramsey"

# print(student1)
# print(student2)
# print(student3)

students = ["Utku","Richard","Ramsey"]
print(students[0])
students.append("James")
students.remove("Richard")
students[1] = "Emma"
print(students)

# list contructor
cities = list(("Ankara","Los Angeles","Berlin"))
print(cities)
print(len(cities))


# other functions
# print(cities.clear())
print("Count of Ankara: " + str(cities.count("Ankara")))
print("Index of Ankara: " + str(cities.index("Ankara")))
cities.pop(1)
cities.insert(0, "London")
cities.reverse()
print(cities)


cities3 = cities.copy()



cities2 = cities
cities2[0] = "Hamburg"
print(cities)
print(cities2)
#SAME POINTER

print(cities3)

cities.extend(cities3)
cities.sort()
cities.reverse()
print(cities)