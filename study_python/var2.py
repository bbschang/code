var = [
	('name',1,2),
	('age','lichangsheng'),
	('name',43,4)
]

def do_name(x,y):
	print('name',x,y)

def do_age(x):
	print('age',x)

for i,*j in var:
	if i =='name':
		do_name(*j)

	if i == 'age':
		do_age(*j)

for i,*j in var:
	print(type(i),type(j))


var = (3,4,5,6)

a,ign,w,c = var

print (a,c,ignore,w)
