# -*- coding: utf-8 -*-
# 进程间通信
from multiprocessing import Process, Queue
import os, time, random

def write(q):
	print('Process to write %s' %os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())
		
def read(q):
	print('Process to read %s' %os.getpid())
	while True:
		value = q.get()
		print('Get %s from queue...' % value)
	
if __name__ == '__main__':
# 	父进程创建Queue并传给子进程
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	
	pw.start()
	
	pr.start()
# 	等待write进程
	pw.join()
	
# 	强行终于
	pr.terminate()