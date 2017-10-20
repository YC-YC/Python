# -*- coding: utf-8 -*-
# 多线程
import os,random,time, threading, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 发送任务队列
task_queue = queue.Queue()
# 接收结果队列
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

def return_task_queue():
    global task_queue
    return task_queue
 
def return_result_queue():
    global result_queue
    return result_queue
def test():
# 把两个queue注册到网络
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    
    # 启动Queue
    manager.start()
    
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 把任务放到队列
    for i in range(10):
        n = random.randint(0, 1000)
        print('Put task %d...' % n)
        task.put(n)
        
    for i in range(10):
#         r = result.get(timeout=10)
        r = result.get()
        print('get result =', r)
    # 关闭
    manager.shutdown()
    print('master exit')

if __name__ == '__main__':
    freeze_support()
    test()
    print('END')