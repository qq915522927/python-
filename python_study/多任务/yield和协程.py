
def customer():
    r = '这是初始化结果'
    while True:
        n = yield r
        print('-----------------')
        r = r+str(n)

g = customer()
print(dir(g))
print(g.send(None))
print('**********')
print(g.send('aaaa'))
print('**********')
print(g.send('bbbb'))
print('**********')
print(g.__next__())
print(next(g))
