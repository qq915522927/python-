#itertools提供了很多生成 迭代器的 工具
import itertools

nutual = itertools.count(1,2) #参数为开始和步长
# for i in nutual:
#     print(i)

nutual2 = itertools.repeat('wu',100)#生成重复一个元素的迭代器
for i in nutual2:
    print(i)

    '''
    还有一些方法：chain,groupby
    以后再学习使用
    '''