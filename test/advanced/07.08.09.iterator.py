# -*- coding: utf-8 -*-
#迭代，只要是可迭代对象都可以迭代
d = {'a':1, 'b':2, 'c':3}
for key in d:
	print('iterator key =', key)

for value in d.values():
	print('iterator value =', value)
	
for item in d.items():
	print('iterator item =', item)
	
for ch in 'ABCD':
	print('iterator ch =', ch)

#判断可迭代
from collections import Iterable

print('str is iterator:', isinstance('abd', Iterable))
print('list is iterator:', isinstance([1,2], Iterable))
print('tuple is iterator:', isinstance((3,4), Iterable))
print('int is iterator:', isinstance(123, Iterable))

#enumerate将list生成index-value
for index,value in enumerate(['A', 'B', 'C']):
	print('index:', index, 'value:', value)
for x, y in [(1,2), (3,4), (5,6)]:
	print(x, y)