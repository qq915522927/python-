# coding=utf8


'''
__len__:计算元素个数，
'''
l = [1,2]
print(len(l))#True

class test1():
    def __len__(self):
        print 'ok'
        return 3

t = test1()
print(len(test1))

#结果
# True
# 3 ok
# True