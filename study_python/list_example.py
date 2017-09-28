
# -*- coding:utf-8 -*-  
#list_example.py
# 学习list

# list可以为空

var = []
print var
print type(var)

#一切可序列化的对象都可以转化为列表
tuble = (1,2,3)
string  = "lichangsheng"

var = list(tuble)
var1 = list(string)

print var,var1

#list可以用下标索引取值

var = [0,1,2,3,4,5,6,7,8,'a']
print var
print var[3],var[5]
print type(var)

#list可以嵌套list，当然也可以用双重下标访问
var = [0,1,2,3,4,5,6,[11,22,33,44],8,'a']
print var
print var[7]
print var[7][1]
print type(var)
#对象与函数都可以做为列表的成员

class Person:
	def face(eyes):
		return eyes
lcs = Person()
var = [1,2,Person,lcs,]
print var,'\n'
print var[2],var[3]

#list 的切片访问

var = [0,1,2,3,4,5,6,[11,22,33,44],8,'a']
print var[3:5]
print var[0:len(var)-1:2]
print var[5:-3]
print var[0:]
print var[-6:-0]
print var[-1]
print var[-0]

#list有相关通用方法

var = [0,1,2,3,4,5,6,[11,22,33,44],8,'a']
print var
#pop(),弹出
var.pop()
var.pop(3)
print var

#del(),删除列表对象
del var[3]
print var

#修改，直接修改就行
var[3] = 'name'
print var

#查长度

print len(var)

#cmp()比较两个列表
var1 = [1,2,3]
var2 = [1,2,3]
var3 = [3,2,1]
print cmp(var1,var2)

#max(),min()
#python#:max(list)或者min(list)的时候，数字与数字比较不用说怎么比较，如果是列表与列表比，是比第表中的第一个元素，字符串大于数字，大于列表

print max(var)
print max(var1)
print max(var3)
print min(var)

var  = [[5,2,3],[4,5,6,7],'zpp',lcs,Person]
print max(var)

#列表可以组合、重复、判断、迭代。

var1 = [1,2,3]
var2 = [4,5,6]
varplus = var1+var2
print var1,var2,varplus

varrepete = var1*5
print varrepete

print 3 in var1
print 3 in var2

for i in var1:print i

#列表可以有的方法
#list.append(),extend(),index(),reverse()
var = range(0,10)
var  = var*3
print var 
var.append('abc')
var.extend(var2)
print var,var.count(4),var.index('abc'),len(var)

var.sort()
print var


var.pop(2)
print var,len(var)

var = range(0,10)
var.reverse()
print var
var.pop(2)
print var
var.pop(var.index(4))
print var


str1 = ('lcs','is','good','boy')

s = ":".join(str1)
print s



