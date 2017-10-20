# -*- coding: utf-8 -*-
# 分布式进程，工作进程
import time, threading
from multiprocessing.managers import BaseManager
class QueueManager(BaseManager):
    pass
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print('Connect to server:', server_addr)
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务，并把结果写入到result队列
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d*%d...' % (n,n))
        r = '%d * %d = %d' %(n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty')
print('worker end')

print('END')