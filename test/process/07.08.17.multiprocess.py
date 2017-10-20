# -*- coding: utf-8 -*-
# 多进程
import os
from multiprocessing import Process
# 子进程执行
def run_proc(name):
	print('Run child process %s(%s)...' % (name, os.getpid()))
	
if __name__ == '__main__':
	print('Parent process %s' %os.getpid())
	p = Process(target=run_proc, args=('test',))
	print('Chile process will run')
# 	启动子进程
	p.start()
# 	等待子进程执行
	p.join()
	print('Parent process end')