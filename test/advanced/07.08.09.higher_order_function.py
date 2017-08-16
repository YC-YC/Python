# -*- coding: utf-8 -*-
#函数式编程，高阶函数
#函数可赋值给一个对象，然后当变量一样传给另一个函数
def add(x, y, f):
	return f(x) + f(y)
print('abs x,y =', add(-4, -6, abs))

#map(),接收两个参数，一个是函数f，一个是Iterable,作用为用f处理Iterable每个元素，处理结果保存到Iterable里并返回
def my_power(x):
	return x*x
r = map(my_power, [1,2,3,4])
#map返回结果为Iterable,为惰性序列
print('map =', list(r))

#reduce,接收两个参数,第一个是函数f,该函数必需要有两个参数，另一个是序列，处理结果为用f从序列开头处理，处理结果和序列下一个元素再处理
#reduce(f,[x1,x2,x3,x4]) = f( f( f(x1,x2),x3), x4)
def add(x, y):
	return x+y
from functools import reduce
print('reduce(add, [1,2,3,4,5]) =', reduce(add, [1,2,3,4,5]))

def str2int(s):
	def fn(x, y):
		return x*10 + y
	def char2num(c):
		return{'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[c]
	return reduce(fn, map(char2num, s))	
print('str2int("123456") =', str2int('123456'))

#filter参数和map一样，f处理结果为True则保留，否则去掉
def is_odd(x):
	return x%2 == 1
r = filter(is_odd, [1,2,3,4])
print('filter(is_odd, [1,2,3,4])) =', list(r))

#sorted
print('filter(is_odd, [1,2,3,4])) =', sorted([-36,]))