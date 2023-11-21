# -*- coding: utf-8 -*-

dictionary = {
    "book" : "kitap",
    "table" : "masa"
    }
dictionary2 = dict(kitap = "book", masa = "table")


# print(dictionary[0])  #can not access with index
dictionary["book"] = "kitap 1"
dictionary["pencil"] = "kalem"

del(dictionary["pencil"])
print(len(dictionary))
print(dictionary["book"])
print(dictionary)