# -*- coding: utf-8 -*-
#列表生成
print('list(range(1,10)):', list(range(1,10)))

print('list(range(1,10)):', [x*x for x in range(1, 10) if x%2 == 0])

import os
print('list cur dir:', [d for d in os.listdir('.')])
print('list cur dir:', [d for d in os.listdir('.') if d.endswith('.py')])

#生成器,由[]改成(),
g = (x*x for x in range(1, 10))
for n in g:
	print(n)