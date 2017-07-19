
#把列表生成式的[]改为()即可
l = (x*x for x in range(10))
for i in l:
    print(i)
for i in l:
    print(i)#遍历一便后，就无法遍历了
# while True:
#     print(next(l))

#用函数创建生成器
#斐波拉契数列
#1, 1, 2, 3, 5, 8, 13, 21, 34
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n += 1
    print('done')
    return
c=fib(3)
while True:
    print(next(c))
while True:
    print(c.__next__())
