from collections import defaultdict

d = defaultdict(list)
print(d)
d['a'].append(1)
d['a'].append(2)
d['a'].append(1)
d['a'].append(3)
print(d)
print(type(d))

d = defaultdict(set)
print(d)
d['a'].add(1)
d['a'].add(2)
d['a'].add(1)
d['a'].add(3)
print(d)
print(type(d))

