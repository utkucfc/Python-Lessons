# -*- coding: utf-8 -*-

number = int(input("Give a number: "))
isPrime = True
for x in range(2, number):
    if(number%x) == 0:
        isPrime = False
        break

if isPrime:
    print("PRIME!")
else:
    print("Not prime.")