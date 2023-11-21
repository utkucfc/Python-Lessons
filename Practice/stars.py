# -*- coding: utf-8 -*-

number = int(input("How many stars do you want: "))
star = ""

for x in range(1, number + 1):
    star = star + "*"
    print(star)