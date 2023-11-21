# -*- coding: utf-8 -*-

f = open("customers.txt")
# f.write("test")
# print(f.read())

for l in f:
    print(l)
    
f.close()


fileToAppend = open("customers.txt", "w")
fileToAppend.write("\n")
fileToAppend.write("Utku")
fileToAppend.close()

import os

if os.path.exists("customers.txt"):
    os.remove("customers.txt")
else:
    print("file not exist.")
    
os.rmdir("empty")