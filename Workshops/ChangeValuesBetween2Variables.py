# -*- coding: utf-8 -*-


x = 10
y = 20


print("x: " + str(x))
print("y: " + str(y))

### first solution
# temp = x
# x = y
# y = temp

### second solution
x,y = y,x

print("x: " + str(x))
print("y: " + str(y))

