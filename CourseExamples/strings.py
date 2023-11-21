# -*- coding: utf-8 -*-

# substring
msg = "Hello World"
print(msg[2:7])
newMsg = msg[10:11]
print(newMsg)

# len
print(len(msg))
newMsg2 = msg[len(msg)-1:len(msg)]
print(newMsg2)

# lower & upper
print(msg.upper())
print(msg.lower())

# replace
msg.replace('o','u')
print(msg) #replaced message not assigned to msg
print(msg.replace('o', 'u'))

#same example but with assignment
msg = msg.replace('o','u')
print(msg)
print(msg.replace('o', 'u'))

# split and strip
data = "Utku CIFCI 25 Ankara"
print(data.split())

data2 = "     Ramiz;KARAESKI;60;Istanbul    ".strip()
print(data2.split(";"))
print("Name: " + data2.split(";")[0])

