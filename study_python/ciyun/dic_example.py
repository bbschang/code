# -*- coding: utf-8 -*-

var = {"d":12,"b":8,"a":55,'age':33}

#,用Key 访问value

print var["d"]

print var

#F增删改

var['name'] = 'lichangsheng'
del(var['age'])
var['b国家标准'] = 23

'''
print var


print str(var['name'])
print type(str(var))

result1 = []
result2 = []

for key in var:
	result1.append(key)
	result2.append(var[key])

print result1,result2


print var.items()

s = sorted(var.items(), cmp = lambda x, y: cmp(x[1], y[1]))

print s
print type(var.items())
print var.items()

'''

list = var.items()
print list

print sorted(list,key = lambda b:b[1])

print



