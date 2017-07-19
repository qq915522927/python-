#coding=utf8

'''
set是一组key的集合，可不能重复
且key不能为可变对象
'''
s = set([1,4,5])
print(s)

s = set([11,22,33,11,11])#重复元素自动过滤
print(s)
s.add(99)#添加
s.remove(11)#移除
print(s)

#可以做数学意义上的交集并集等
s1 =set([1,2,3])
s2 = set([2,3])

print(s1&s2)#交集

print(s1|s2)#并集