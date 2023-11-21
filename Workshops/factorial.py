# -*- coding: utf-8 -*-

number = int(input("Give a number: "))

factorial = 1

if number < 0:
    print("Can not calculate factorials on negative numbers")
elif number == 0:
    print("Result: 1")
else:
    for i in range(1, number + 1):
        factorial = factorial * i
    print("Result: ", factorial)