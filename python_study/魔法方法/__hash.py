'''
__hash__对应hash()
'''

print(hash(1))

#实际上若对象没有重写hash方法，返回的hash码是内存地址计算的
#重写后返回 return值
class test():
    def __hash__(self):
        return 666
t = test()
print(hash(t))


# print(hash([343]) unhashable type: 'list'
#猜测 可以hash的为不可变对象，不能hash的为可变对象
#list，dict，set不能通过地址确定值得唯一性，因而无法hash