import os
import time
a = os.fork()
print(a)
if a==0:
    while True:
        print(1)
        time.sleep(1)

else:
    time.sleep(3)
    print('end')
