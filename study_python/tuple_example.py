#-*- coding:utf-8 -*-

# tuple 是不变的list,定义之后就不能增，删，改。

s = ("李昌盛","gyp","rzy")

var = ('q','e',2,'3','e',4)
print var,type(var)

# tuple 也可以索引与切片

print var[2],var[0:1],var[1:-1],var[0:-1]


#可序列化的对象

for i in var:print i,type(i)

#index(),max()

print var.index('e'),max(var),min(var),len(var)