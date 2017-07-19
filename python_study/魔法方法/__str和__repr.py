#__str__方法是指定打印给用户看的对象信息

class Dog(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

d = Dog('小黄')
print(d)

#__repr__方法用于显示程序开发者的字符串,可以调用repr()函数查看

print(repr(d))

