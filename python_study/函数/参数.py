

#默认参数

def test(l=[]):
    l.append('end')
    return l
a = test()
print(a)
a = test()
print(a)
a = test()
print(a)
a = test([3])
print(a)

#默认参数尽量不用可变对象，会导致默认参数的变化
def test(l=None):
    if l is None:
        l = []
    l.append('end')
    return l
a = test()
print(a)
a = test()
print(a)
a = test()
print(a)
a = test([3])
print(a)


'''关键字参数'''
def test2(**kwargs):
    print(kwargs)
    print(kwargs.items())
    for x,y in kwargs.items(): #dict_items([('a', 'b'), ('d', 5)])
        print(x,y)

test2(a='b',d=5)

'''命名关键字参数
指定关键字参数为指定字段'''
def test5(a,b,*,c,d):
    pass

# 必须要传入 指定的命名关键字
test5(1,1,c=1,d=3)
