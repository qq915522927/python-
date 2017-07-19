# coding=utf8


'''
__contains__:判断是否包含 元素， x in s
'''
l = [1,2]
print(1 in l)#True

class test1():
    def __contains__(self, item):
        print item,'ok'
        return True

t = test1()
print(3 in t)

#结果
# True
# 3 ok
# True