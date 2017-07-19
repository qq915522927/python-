#getitem方法实现后可以用对象向列表的下标一样取元素
#l[1]


class Fib(object):
    def __getitem__(self, item):
        a,b = 1,1
        for x in range(item):
            a,b = b,a+b
        return a

f = Fib()
print(f[1])
print(f[3])
