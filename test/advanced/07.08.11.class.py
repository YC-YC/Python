# -*- coding: utf-8 -*-
# 类，
# 成员变量、函数添加__，为private，但可以强制zhangsan._Student__name这样调用
# __xxx__为特殊函数
# 成员变量、函数添加_，为protected,子类可以调用

class Student(object):
# 	类属性，每个类了实例都共有
	attr = 'Student'
# 	构造方法
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
# 	成员方法都以self参数开头
	def print_score(self):
		print('%s, %s' %(self.__name, self.__score))
		
zhangsan = Student('ZhangSan', 59)
lisi = Student('LiSi', 99)
zhangsan.print_score()
# print('zhangsan name is:', zhangsan.name)
print('zhangsan name is:', zhangsan.get_name())
# 添加新成员
zhangsan.age = 8
print('zhangsan age is:', zhangsan.age)
lisi.print_score()


# 类继承
class ZhangSan(Student):
	def print_score(self):
		print('ZhangSan:%s, %s' %(self.get_name(), self.get_score()))
class LiSi(Student):
	pass
zhangsan = ZhangSan('ZhangSan', 58)
zhangsan.print_score()

# 类信息获取
print('type(zhangsan) =', type(zhangsan))
# dir获取所有属性和方法
print('dir(zhangsan) =', dir(zhangsan))
# 通过hasattr,getattr,setattr可操作属性
print('hasattr print_score =', hasattr(zhangsan, 'print_score'))

# __slot__限定属性，子类不起作用
class Animal(object):
	__slots__ = ('name', 'age')
	
animal = Animal()
animal.name = 'Dog'
animal.age = 5
# 没限定的不能添加
# animal.home = 'BeiJin'

class Teacher(object):
	@property
	def name(self):
		return self._name
	
# 	如果没定义，_name相当为只读
	@name.setter
	def name(self, n):
		if not isinstance(n, str):
			raise ValueError('name must be str')
		self._name = n

	@name.getter
	def name(self):
		return self._name

t = Teacher()
# t.name = 123
# 相当调用set_name
t.name = 'LiLaoShi'
# 相当调用get_name
print(t.name)


