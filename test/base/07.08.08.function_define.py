# -*- coding: utf-8 -*-
#可配置默认参数，但必需放在后面
def power(x, n = 2):
	s = 1
	while n > 0:
		n = n -1
		s = s * x
	return s

print('2power5 = ', power(2, 5))
print('4power2 = ', power(4))

#默认参数副作用
def add_end(L = []):
	L.append('END')
	return L

print('add_end = ', add_end([1, 2, 3]))

#默认参数L在函数定义时就已经确认，当改变时就下次就为改变后的值
print('add_end = ', add_end())
print('add_end = ', add_end())
print('add_end = ', add_end())

#因此默认参数应指向一个不变对象
def add_end2(L = None):
	if L is None:
		L = []
	L.append('END')
	return L
	
print('add_end = ', add_end2())
print('add_end = ', add_end2())
print('add_end = ', add_end2())


#########可变参数,参数前面带*，参数自动转成tuple
def calc(*number):
	sum = 0
	for x in number:
		sum = sum + x * x
	return sum
	
print('calc(1, 2) = ', calc(1, 2))
print('calc(1, 2, 3) = ', calc(1, 2, 3))

nums = [1, 2, 3]
#list前面加*表示将list的每个元素当作参数传入
print('calc list = ', calc(*nums))


############关键字参数,自动装成dict
def person(name, age, **kw):
	print('name =', name, ',age =', age, ',other =', kw)

person('ZhangSan', 30)
person('ZhangSan', 30, city = 'BeiJin')

extra = {'city':'BeiJin', 'Job':'Teacher'}
#**允许将dict
person('ZhangSan', 30, **extra)

#########命名关键字，限定参数名称
#def person(name, age, *args, city, job):当有可变参数时，不用写*
def person2(name, age, *, city, job):
	print('name =', name, ',age =', age, ',city =', city, ',job =', job)
def person3(name, age, *args, city, job):
	print(name, age, args, city, ',job =', job)
#参数需要传入参数名
person2('ZhangSan', 30, city = 'ShangHai', job = 'IT')
person3('ZhangSan', 30, city = 'ShangHai', job = 'IT')


######组合参数
def f1(a, b, c =0, *args, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c =0, *, d, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
	
#在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去
f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', city = 'BeiJin')
f1(1, 2, 3,  city = 'BeiJin')

f2(1,2, d='hello', ext = 'Note')

args=[1,2,3,4]
kw = {'d':99, 'extra':None}
f1(*args, **kw)
args=[1,2,3]
f2(*args, **kw)
#所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
