# -*- coding: utf-8 -*-
#生成器,保存算法，执行时才计算结果
g = (x*x for x in range(10))
for n in g:
	print('get :', n)
	
#斐波拉契数列
def fib(max):
	n,a,b=0,0,1
	while n < max:
		print(b)
		a,b = b,a+b
		n = n+1
	return 'Done'
fib(6)

#改造成genarator,遇到yield停止，next时从上一个yield开始执行，
def fib2(max):
	n,a,b=0,0,1
	while n < max:
		yield b
		a,b = b,a+b
		n = n+1
	return 'Done'
g = fib2(7)
#for拿不到函数的返回结果，如果想要拿到返回结果，需要手动调用next，并监听StopInterator
for n in g:
	print('get :', n)

while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('genarator return value is:', e.value)
		break
		
#杨辉三角
#		   1
#        1   1
#      1   2   1
#   1   3   3   1
#  1   4   6   4   1
#1   5   10  10  5   1

def add_list(tmpList):
	lst = [1]
	last = 0
	for num in tmpList:
		if last == 0:
			last = num
		else:
			lst.append(num+last)
			last = num
	lst.append(1)
	return lst

def triangles():
	row = 1
	L = [1]
	while True:
		yield L
		L = add_list(L)
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break




