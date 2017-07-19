#可以作用于for循环便利的称为iterable
#生成器和list,dict等都是iterable
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
a = iter([1,3,3])
print(a)

#Python的for循环本质上就是通过不断调用next()函数实现的,现将iterable
#转化为iterator

