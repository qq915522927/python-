#encoding=utf8

from multiprocessing import Pool
import time
import os

def worker(num):
    time.sleep(1)
    print('工人 = %d，任务 = %d '%(os.getpid(),num))
    
pa = Pool(3)
for i in range(10):
    print(i)
    pa.apply_async(worker,(i,))
print('start')
pa.close()
pa.join()
print('end  ')

