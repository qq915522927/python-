#
# threadLocal作为全局变量，保存着各个线程中的局部变量，相当于一个全局字典，在每个自己的线程中
# 都能拿到自己的局部变量

import threading

local = threading.local()

def threading_task(name):
    l = list((name,))
    local.list = l
    print_list()

def print_list():
    print(local.list)


t1 = threading.Thread(target=threading_task,args=(1,))
t2 = threading.Thread(target=threading_task,args=(2,))
t3 = threading.Thread(target=threading_task,args=(3,))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print('end')
