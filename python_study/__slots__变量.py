#__slots__变量可以限制实例对象可以设置的属性
'''
它的值为一个元祖
'''
class People(object):
    __slots__=('name','age')

p = People()
p.name = 'sdf'
p.gender = '男'  #AttributeError: 'People' object has no attribute 'gender'