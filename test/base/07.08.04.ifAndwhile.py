# -*- coding: utf-8 -*-
age1 = input('input age:')
age = int(age1)
if age > 2000:
	print('00后')
elif age > 1990:
	print('90后')
else:
	print('其它')

names = ('ZhangSan', 'LiSi', 'WangWu')
for name in names:
	print('name =', name)
	
sum = 0
for i in list(range(100)):
	sum += i
print('sum =', sum)