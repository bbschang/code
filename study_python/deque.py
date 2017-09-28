from collections import deque


var = deque(maxlen = 3)

print(var)

var.append(3)
var.append(2)
var.append(1)


print(var,var[0])

print(type(var))