#orderddict_example.py

from collections import OrderedDict
import json


var = OrderedDict()

print(type(var))

var['name'] = 1
var['age'] = 2
var['class'] =3
var['age'] = 4

print(var)

json1 = json.dumps(var,4)

print(json1)
