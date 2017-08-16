# -*- coding: utf-8 -*-
#递归函数,递归会造成栈溢出
def fact(n):
	if n == 1:
		return 1
	return n*fact(n-1)

print('fact -->', fact(100))

#尾递归，返回值不包括表达式,python没做优化，无法实现
def fact2(n):
	return fact_inter(n, 1)

def fact_inter(num, sum):
	if num == 1:
		return sum
	return fact_inter(num -1, num*sum)
	
print('fact -->', fact2(100))
