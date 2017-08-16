classmate = ['张三', 'LiSi', 'WangWu']
print('list len() =',len(classmate))
print(classmate[1])
print(classmate[-2])
classmate.append('ZhaoLiu')
print('classmate =', classmate)
classmate[0] = 'ZhangSan'
print('classmate =', classmate)
classmate.insert(0, 'WangBa')
print('classmate =', classmate)
classmate.pop(0)
print('classmate =', classmate)
LIST1 = ['asp', 'php']
LIST2 = ['python', 'java', LIST1, 'scheme']
print('LIST2 =', LIST2,'len =', len(LIST2))

#tuple,类似list，但元素无法修改
tuple = ('Michael', 'Bob', 'Tracy')
print('tuple =', tuple)
#不是tuple,而是简单的赋值
tuple1 = (1)
print('tuple1 =', tuple1)
tuple2 = (1,)
print('tuple2 =', tuple2)
#可变tuple
LIST3 = ['X', 'Y']
tuple3 = ('A', 'B', LIST3, 'C')
print('tuple3 =', tuple3)
tuple3[2][0] = 'x'
tuple3[2][1] = 'y'
print('tuple3 =', tuple3)