# -*- coding: utf-8 -*-
#切片,list，tuple,str都可以切片处理
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
 
print('list is', L)
print('\n')
print('cut --> 0:3', L[0:3])
print('cut --> :3', L[:3])
print('cut --> 3:', L[3:])
print('cut --> -2:-1', L[-2:-1])

L2 = list(range(1, 100))
print('list is', L2)
print('list is', L2[:50:2])

print('list is', (0,1,2,3,4,5)[:3])

print('cut str', 'ABCDEFG'[::2])