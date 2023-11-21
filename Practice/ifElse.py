# -*- coding: utf-8 -*-

lights = ["red","yellow","green"]
lights2 = ["red","yellow","pink"]

currentLight = lights[2]
currentLight2 = lights2[2]

print(currentLight)

if currentLight == "red":
    print("STOP!")
if currentLight == "yellow":
    print("READY!")
if currentLight == "green":
    print("GO!")
    
    
    
if currentLight2 == "red":
    print("STOP!")
elif currentLight2 == "yellow":
    print("READY!")
else:
    print("GO!")
    