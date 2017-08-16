# -*- coding: utf-8 -*-
# 序列化
import pickle
import json
d = dict(name='YC', age=27, score=100)
print('serial dict =', pickle.dumps(d))

f = open('dump.txt','wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print('reserial dict =', d)

#json转换
json_str = json.dumps(d)
print('json dumps dict =', json_str)
d = json.loads(json_str)
print('json loads dict =', d)

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2Dict(std):
    return{
        'name':std.name,
        'age':std.age,
        'score':std.score
           }
def dict2Student(d):
    return Student(d['name'], d['age'], d['score'])
# 类的转换需要写转换函数和反转函数
s = Student('YC', 27, 99)
std_str = json.dumps(s, default=student2Dict);
print('json dumps Student =', std_str) 
# 使用默认的转化函数__dict__
std_str = json.dumps(s, default=lambda obj:obj.__dict__);
print('json dumps Student by dict =', std_str)  
s = json.loads(std_str, object_hook=dict2Student)
print('json loads Student =', s)   
print('END')