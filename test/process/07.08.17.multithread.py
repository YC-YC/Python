# -*- coding: utf-8 -*-
# 多线程
import time, threading
# 加锁
lock = threading.Lock()

balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def loop():
	print('thread %s is running' % threading.current_thread().name)
# 	n = 0
# 	while n < 5:
# 		n = n+1
# 		print('thread %s >>>%d' % (threading.current_thread().name, n))
# 		time.sleep(1)
	for i in range(1000000):
		lock.acquire()
		try:
			change_it(i)
		finally:
			lock.release()
	print('thread %s end' % threading.current_thread().name)
	
print('thread %s is running' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t2 = threading.Thread(target=loop, name='LoopThread2')
t.start()
t2.start()
t.join()
t2.join()	
print('thread %s end' % threading.current_thread().name)
print('END balance =', balance)