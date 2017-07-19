def f1():
    print('f1')
    while True:
        print('1')
        yield None

def test():
    print('test')

def f2():
    print('f2')
    while True:
        print('2')
        yield None
a = f1()
b = f2()
for i in range(10):
    print('-------')
    a.__next__()
    b.__next__()
    
