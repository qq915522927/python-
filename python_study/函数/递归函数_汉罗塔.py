


def move(n,a,b,c):
    '''
    :param n:盘子个数
    :param a: 起始点
    :param b: 缓冲区
    :param c: 终点
    :return:
    '''
    if n == 1:
        print('%s-->%s'%(a,c))
        return

    move(n-1,a,c,b)
    move(1,a,b,c)
    move(n-1,b,a,c)

move(3,'A','B','C')
