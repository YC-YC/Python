# -*- coding: utf-8 -*-
# 类多重继承
class Animal(object):
	pass
# 哺乳类
class Mammal(Animal):
	pass
# 飞禽类
class Bird(Animal):
	pass

class Dog(Mammal):
	pass

class Bat(Mammal):
	pass

class Parrot(Bird):
	pass
class Ostrich(Bird):
	pass

class Runnable(object):
	def run(self):
		print('running...')
		
class Flyable(object):
	def fly(self):
		print('flying...')
# 多重继承
class FlyableBat(Mammal, Flyable):
	pass

b = FlyableBat()
b.fly()


# 枚举类型
from enum import Enum
Month = Enum('MyMonth',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan)
print(Month['Feb'])
print(Month.Jan.value)

from enum import Enum, unique
@unique
class Weekday(Enum):
	Sun = 0 # Sun的value被设定为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6