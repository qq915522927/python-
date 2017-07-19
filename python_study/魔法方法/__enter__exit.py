#只要实现了__enter__和__exit__方法的对象是咧，就可用
#with as 语句来调用

#类文件对象是在exit里进行close,发生错误也会关闭
#enter和exit 是在 with 进入代码块前前和后分别执行的
class Son(object):
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print('%s诞生了'%self.name)
        return  'result'
    def __exit__(self, exc_type, exc_val, exc_tb):

            print('顺利诞生')


s = Son('wu')
with s as g:
    print(g)
    print(s.name)