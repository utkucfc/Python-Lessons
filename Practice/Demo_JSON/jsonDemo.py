# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:17:06 2023

@author: Admin
"""

import json

# data = '{"name":"ahmet","surName":"mehmet"}'
# dataJson = json.loads(data)

# print(dataJson["surName"])

# print(type(dataJson))

# customer = {
#     "isim":"veli",
#     "soyisim":"ali",
#     "telefon":"05555555555"
#     }

# customerJson = json.dumps(customer)

# print(type(customerJson))


with open("data.json") as users:
    data = json.load(users)
    
    for d in range(10):
        
        print("########################################")
        print("********USER DATA********")
        print(data[d]["name"])
        print(data[d]["email"])
        print(data[d]["address"]["street"])
        print(data[d]["address"]["suite"])
        print(data[d]["address"]["city"])
        print(data[d]["phone"])
        print("********COMPANY********")
        print(data[d]["company"]["name"])
        print(data[d]["company"]["bs"])
        print(data[d]["name"])