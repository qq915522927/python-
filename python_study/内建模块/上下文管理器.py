#上下文管理器对应contextlib模块
import contextlib


@contextlib.contextmanager
def get_file(filename):
    print('正在打开文件')
    f = open(filename,'r',encoding='utf8')  #代码块执行前的准备工作
    yield f
    print('正在关闭文件')
    f.close()#执行后的善后工作

with get_file('test.py') as g:
    print('正在读取文件')
    print(g.read())


