

#当创建一个实例时调用__new__,并返回实例对象

class A(object):
    def __new__(cls, *args, **kwargs):
        print('正在创建是咧')
        return super().__new__(cls, *args, **kwargs)


a = A()
print(a)
