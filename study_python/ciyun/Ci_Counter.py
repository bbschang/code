
from collections import Counter
import jieba.analyse
import time



bill_path = r'ci.txt'
bill_result_path = r'ci_result.txt'
#car_path = 'car.txt'

with open(bill_path,'r') as fr:
	data = jieba.cut(fr.read())
data = dict(Counter(data))

newvalue = [ v for v in sorted(data.values())]

for k,v in data.items():print k,v

with open(bill_result_path,'w') as fw:
    for k,v in data.items():
        fw.write("%s,%d\n" % (k.encode('utf-8'),v))
