from multiprocessing import Queue,Process
import time
import os
def getNews(q):
    print('接受进程%d开始...'%os.getpid())
    while True:
        if q.empty():
            print('数据空了,等待装载...')
            time.sleep(1)
            if q.empty():
                print('彻底没了')
                break
            else:

                value = q.get()
                print('得到新闻内容为：%s'%value)

        else:
            value = q.get()
            print('得到新闻内容为：%s'%value)

def setNews(q):
    for i in '伍志文是大叔阿比':
        print('放入queue队列的消息为：%s'%i)
        q.put(i)

q = Queue(4)
p1 = Process(target=setNews,args=(q,))
p2 = Process(target=getNews,args=(q,))
p1.start()
p2.start()
p1.join()
p2.join()

