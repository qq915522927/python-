def onclick(func,name):
    print('触发点击事件')
    func(name)

def alert(name):
    print('alert:%s'%name)


onclick(alert,'wu')