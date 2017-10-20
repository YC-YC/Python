# -*- coding: utf-8 -*-
# 批量创建多进程
import os
from multiprocessing import Pool
import time, random
import subprocess
# 子进程执行
def long_time_task(name):
	print('Run Task[%s], pid = %s ...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random()*3)
	end = time.time()
	print('Task[%s] run time = %0.2f ...' % (name, (end - start)))
	
if __name__ == '__main__':
	print('Parent process %s' %os.getpid())
# 	最多执行子进程个数
	p = Pool(4)
	for i in range(5):
# 		添加新进程
		p.apply_async(long_time_task, args=(i,))
	print('wait for child process ...')
# 	close后就不能再添加新进程
	p.close()
	
# 	等待所有子进程执行
	p.join()
	print('All subprocesses done')
	
	
# 	有返回结果的子进程
	print('$ nslookup www.python.org')
	r = subprocess.call(['nslookup', 'www.python.org'])
	print('return code:', r)
	
	
	
	
	