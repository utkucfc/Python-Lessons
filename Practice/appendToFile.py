# -*- coding: utf-8 -*-

students = ["Utku","Leo","Don","Raph","Mike"]

fileToAppend = open("students.txt", "a")

for student in students:
    fileToAppend.write(student)
    fileToAppend.write("\n")

fileToAppend.close()