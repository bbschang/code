#现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？

# var = (3,4,5,2,3,4,5,6)
# var1 = 3,
# var2 = 4,
#......


var = (3,4,5,2,3,4,5,6)
result = []
for i in range(0,len(var)):
	result.append(0) 

for i in range(0,len(var)):
	result[i] = var[i]
	print(result[i])

a,b,c,d,e,f,g,h= result
print(a,b,c)


*c,b = var
print (sum(c))

print(c)