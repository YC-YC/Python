# -*- coding: utf-8 -*-
# 文件操作
from _ast import Try
f = open('test.txt', 'r')
print(f.read())
f.close()

# try:
# 	f = open('test2.txt', 'r')
# 	print(f.read())
# finally:
# 	if f:
# 		f.close()

try:
# 	封装open和close方法
	with open('test2.txt', 'r') as f:
		print(f.read())
except Exception as e:
	print()
	
with open('test.txt', 'r') as f:	
	for line in f.readlines():
		print('read line =', line.strip())#去除末尾'\n'

with open('test.txt', 'r+', encoding='utf-8') as f:
	num = 1
	while True:
		line = f.readline()
		if not line:
			print('read end')
			f.write('\nHello,world')
			break
		print('read line %d =' % num, line.strip())#去除末尾'\n'
		num = num + 1
	
print('END')