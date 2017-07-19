# 当调用实例属性时，属性若不存在，则会以此属性作为参数去调用，__getattr__方法

class Dog():
    def __getattr__(self, item):
        return 'ok'


d = Dog()
print(d.name)


class Chain(object):
    '''
    此类会以 Chain().name.age的方式拼接出一个/name/age的路径字符串
    '''

    def __init__(self,path=''):
        self.path = path
    def __getattr__(self, item):
        self.path = self.path + '/' +item
        return self

    def __str__(self):
        return  self.path

u = Chain().user.login
print(u)
p =  Chain().user.login.path
print(p)

