# -*- coding: utf-8 -*-

x = [[1,3,5],[2,4,1],[1,5,7]]
y = [[3,3,4],[2,4,1],[3,5,4]]

sum = [[0,0,0],[0,0,0],[0,0,0]]

# sum[0][0] = x[0][0] + y[0][0]
# sum[0][1] = x[0][1] + y[0][1]
# sum[0][2] = x[0][2] + y[0][2]
# etc....

for i in range(len(x)):
    for j in range(len(y)):
        sum[i][j] = x[i][j] + y[i][j]

print(sum)

