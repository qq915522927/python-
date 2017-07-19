#元类是用来创建类的模板
print(type(5))
print(type(int))
# <class 'int'>
# <class 'type'>
# 可以看出类是type的一个实例



# 定义元类,要继承与type
class DogMetalClass(type):
    def __new__(cls, name,bases,attrs):
        '''

        :param name: 要创建的类名
        :param bases: 要创建类的父类
        :param attrs: 类的方法集合
        :return: 通过元类产生的类
        '''
        print('name:%s'%name)
        print('bases%s'%bases)
        print('attrs:%s'%attrs)
        name = 'Dog2'
        attrs['run']=lambda slef,name:print('%s狗在跑'%name)
        return type.__new__(cls, name,bases,attrs)


class Dog(object,metaclass=DogMetalClass):
    pass

d=Dog()
d.run('惊云') #Dog类没有定义run()方法，是元类在创建Dog类的时候动态添加的
print(Dog.__name__)