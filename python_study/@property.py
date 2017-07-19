#@property装饰器可以将类中的方法转化为属性的调用方式，成为getter和setter

'''
两个方法的名称要相同
通过getter和setter就能管理对象的属性，或者是设置提取权限和设置条件
'''
class Dogs(object):
    def __init__(self,value):

        self._name=value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if isinstance(value,int):
            print('不能位数字')
            return
        self._name = value


xiaohuang = Dogs('小黄')
xiaohuang.name = '小绿'
xiaohuang.name =44

print(xiaohuang.name)

