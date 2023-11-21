# -*- coding: utf-8 -*-

studentsSet = {"Donatello","Leonardo","Michelangelo","Raphael"}
print(studentsSet)

for student in studentsSet:
    print(student)
    
if "Donatello" in studentsSet:
    print("This is in the list")
    
studentsSet.add("Splinter")
print(studentsSet)

studentsSet.update(["Don","Leo","Mike","Raph"])
print(studentsSet)

print(len(studentsSet))

studentsSet.remove("Don")
print(len(studentsSet))

studentsSet.discard("Don")
print(len(studentsSet))

x = studentsSet.pop()
print(studentsSet)

studentsSet.clear()
print(len(studentsSet))

del studentsSet
print(studentsSet)

