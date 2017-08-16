# -*- coding: utf-8 -*-
#函数作为参数返回,但此时并没有执行代码结果，只有在调用f()后才执行
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 2, 3, 4)
print('lazy_sum =', f())

#匿名函数
print('lambda function =', list(map(lambda x:x*x, [1, 2, 3, 4, 5])))

#装饰器
import functools
def log(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        print('call %s()' % f.__name__)
        return f(*args, **kw)
    return wrapper
@log
def now():
    print('2017.08.10')

print('now.__name__ =', now.__name__)
now()
# 装饰器可传参数,加多层封装
def log(str):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            print('call %s(%s)' % (f.__name__, str))
            return f(*args, **kw)
        return wrapper
    return decorator

@log('excute')
def now2():
    print('2017.08.10')
    
now2()
