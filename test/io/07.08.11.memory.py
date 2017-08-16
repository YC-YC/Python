# -*- coding: utf-8 -*-
# 内存IO操作StringIO,
from io import StringIO
from _io import BytesIO
f = StringIO()
f.write('Hello,')
f.write('World!')
print('read String IO:', f.getvalue())
	
f = StringIO('Hello!\nHi!\nGoodbye!')	
while True:
	line = f.readline()
	if not line:
		print('read end')
		break
	print('read line =', line.strip())#去除末尾'\n'
	
f = BytesIO()
print('write byte len =', f.write('测试中文123abd'.encode('utf_8')))
print('read BytesIO:', f.getvalue())

print('END')