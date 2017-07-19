# coding=utf8


'''
__iter__:决定对象是否可以迭代
'''
l = [1,2]
for i in l:
    print(i)

class test1():
    def __init__(self):
        self.num = 0
    def __iter__(self):
        self.num += 1
        #必须返回迭代器，也就是实现了__next__()方法的对象,这个对象本身实现了__next__()
        return self
    def __next__(self):#实现__next__方法的类称为迭代器
        print('调用next')
        self.num +=1
        if self.num>=10:
            raise StopIteration()
        return self.num
t = test1()
for i in  t:
    print(i)

'''for 的本质是不断调用迭代器的next方法，
当对象不是迭代器时调用__iter__方法，此方法必须返回一个迭代器。
迭代器又包括生成器和实现__next__的类
'''

for x in (x for x in range(10)):
    print(x)

l = ['s',234,423]
g = l.__iter__()#返回一个生成器
print(g.__next__())
print(g.__next__())
print(g.__next__())
