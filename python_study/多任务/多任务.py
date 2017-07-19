import os
import time
ret = os.fork()
print('ret = %d' %ret)
print(os.getpid())
if ret == 0:
    print('子进程...')
    
    print(os.getpid())
    print('-'*10)
    print(os.getppid())

    time.sleep(5)
    print('子进程over...')

else:
    print('主进程...')
    print(os.getpid())
    time.sleep(2)
    print('主进程over...')
    


