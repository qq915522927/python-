'''
线程是操作系统的最小执行单元，每个进程下至少有一个线程
线程与进程最大的不同在于，进程中的变量都是相互独立的，都拷贝了一份在各自的内存中，而线程
对于变量则是公用的，每个线程都可以修改变量，而修改过程是由操作系统调配的，容易造成数据的混乱，
这时需要给线程加个锁，保证在改变变量时，只有一个进程在操作

python对多线程的支持不好，python解释器中有gil锁
对于io的访问还是可以使用多线程
'''
import threading

balance = 0
lock = threading.Lock()

def change(i):
    global balance
    balance += i
    balance -= i

def thread_task(i):
    '''
    加锁：lock.acquire()
    释放锁：lock.release()

    '''
    for x in range(100000000):
        with lock as f:

            change(i)

if __name__ == '__main__':
    t1 = threading.Thread(target=thread_task,args=(5,))
    t2 = threading.Thread(target=thread_task,args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)

