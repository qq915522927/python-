#把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling


#使用pickle模块实现序列化
#pickle的序列化只能是python内部使用，而且个版本不兼容,只用来保存不重要的对象信息

'''
json是序列化的标准格式，是一个字符串，适用于不同语言的传递，且结构简单，传输快
'''
import json
d =dict(name='dog',age=18)
j = json.dumps(d)
print(j)
print(type(j))

l = json.loads(j)
print(type(l))
print(l)


'''
对于自定义的类型，json不知如何序列化，这是要传入一个参数函数，告诉json序列化对象的方法
也就是将对象的属性和值，用字典表示
'''
def obj2dict(obj):
    return obj.__dict__

class Teacher(object):
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

t = Teacher('wu',18,'男')

j = json.dumps(t,default=obj2dict)
print(j,type(j))

#反序列化同时也需要 提供一个转换函数，返回对象