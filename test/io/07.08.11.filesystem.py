# -*- coding: utf-8 -*-
# 文件系统
import os
from shutil import copyfile
name = os.name
print('platform =', name)
if not 'nt' == name:
	os.uname()
print('environ =', os.environ)
print('当前路径的绝对路径  =', os.path.abspath('.'))
new_path = os.path.join(os.path.abspath('.'), 'testdir')
print('当前路径新建文件夹=', new_path)
if os.path.exists(new_path):
	print('已经存在',new_path)
else:
	print('新建文件夹:',os.mkdir(new_path))

os.rmdir(new_path)
if os.path.exists(new_path):
	print('文件没删除',new_path)
else:
	print('已经删除:',new_path)
copyfile('test2.txt', 'test_new.txt')
os.renames('test_new.txt', 'test_new2.txt')
os.renames('test_new2.txt', 'test_new.txt')
os.remove('test_new.txt')

print('list file =', [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])


print('END')