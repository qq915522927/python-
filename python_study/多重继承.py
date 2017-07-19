#多重继承，即继承多个父类，一般要在主线类上增加其他类的功能，这种设计方式称为MixIn

class Anmials(object):
    pass
class RunableMixIn(object):
    pass

class Dog(Anmials,RunableMixIn):
    pass
'''
Dog类继承了Anmials，同时加入了Runable的功能
'''