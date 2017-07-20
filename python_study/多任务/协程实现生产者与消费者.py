
def customer():
    r = ''
    while True:
        n = yield r

        print('接受到商品%s,正在处理商品..'%n)
        r = 'ok'
        print('处理完毕正在返回消息给生产者')

def producer(g):
    '''
    :param g:消费者生成器
    :return:
    '''
    g.send(None)
    for i in range(3):
        print('生产了商品%s'%i)
        b = g.send(i)
        print('消费者回馈的消息是%s'%b)


g =customer()
producer(g)