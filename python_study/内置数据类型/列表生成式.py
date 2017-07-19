
l = [x*x for x in range(10)]
print(l)

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

l = [x*x for x in range(10) if x%2==0]
print(l)

#可以使用两层循环，可以生成全排列
l = [x+y for x in 'abc' for y in 'efg']
print(l)

#列表生成式也可以使用两个变量来生成list
d = {'a':'A','b':'B'}
l = [x+y for x,y in d.items()]
print(l)
