#groupby_list_dic.py
from operator import itemgetter
from itertools import groupby


rows = [
	{'name':'lichangsheng','date':2017-07-01,},
	{'name':'lichangsheng2','date':2017-07-01,},
	{'name':'lichangsheng3','date':2017-07-02,},
	{'name':'lichangsheng4','date':2017-07-01,},
	{'name':'lichangsheng5','date':2017-07-03,},
	{'name':'lichangsheng6','date':2017-07-02,},
	{'name':'lichangsheng6','date':2017-07-03,},
]

print(rows)

rows.sort(key = itemgetter('date'))

print(rows)

for date,items in groupby(rows,key = itemgetter('date')):
	print(date)
	for i in items:
		print('-----',i)