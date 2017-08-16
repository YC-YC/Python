# -*- coding: utf-8 -*-
#dict，key值不能为可变对象，value随意，类似java的map，但比map更强大，map需要指定固定的key-value对象
d = {'ZhangSan':80, 'LiSi' : 85, 'WangWu': 90}
score = d['ZhangSan']
if score>85:
	print('good')
else:
	print('not good')
d['ZhaoLiu'] = 100
print('add ZhaoLiu =', d['ZhaoLiu'])

print('ZhaoLiu in dict =', 'ZhaoLiu' in d)

print('ZhaoLiu score =', d.get('ZhaoLiu', 0))

d.pop('ZhaoLiu')
print('remove ZhaoLiu dict =', d)


#set,内容不可重复，和java的set一样
s = set([1, 2, 3])
print('set = ', s)
s.add(4)
print('set = ', s)
s.remove(2)
print('set = ', s)

s2 = set([2, 3, 4])
#两个set可做交集，并集处理
s3 = s & s2
print('two set & = ' , s3)
s4 = s | s2
print('two set | = ' , s4)

#可变对象，dict和set的key值都不能为可变对象

l = ['c', 'b', 'a']
print('original list =', l)
#操作的是原对象，所以原对象会变
l.sort()
print('sort list =', l)

a = 'abc'
print('original str =', a)
#生成一个新的对象，原对象保留，所以不可变
a.replace('a', 'A')
print('replace str =', a)
