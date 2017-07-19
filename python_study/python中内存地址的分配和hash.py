#coding=utf8

def a():
    pass
print(a)
print(id(a))
b= hash(a)
print(b*16+8)
print(hex(b))

#猜测
#hash码值与对象的内存地址有一定关系


#实际上若对象没有重写hash方法，返回的hash码是内存地址计算的
#重写后返回 return值
class test():
    def __hash__(self):
        return 666
t = test()
d={t:4,8:9}

print(hash(t))
