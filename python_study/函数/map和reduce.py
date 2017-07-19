
#map接受两个参数，第一个参数为函数，第二个参数为lterable,iterable对象里的每个
#元素都作为参数，传入前一个参数函数,并返回一个itrator惰性序列
from functools import reduce


def f1(x):
    return  str(x)

r = map(f1,[3,4,5,6])
print(r)
print(next(r))
l = list(r)
print(l)

#reduce
#reduce接受两个参数，第一个参数为函数，第二个参数为iterable对象,函数先作用前两个元素,然后
#用结果和后一个元素作为参数传入函数

def add(x,y):
    return  x*10+y

r = reduce(add,[1,2,3,4,5,])
print(r)
