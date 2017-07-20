import asyncio
import datetime
import time


@asyncio.coroutine
def hello():
    print('任务一 开始了!')
    print('执行中')
    print('遇到了费时操作')
    r = yield from asyncio.sleep(5)
    print(str(r))
    print('任务一 费事操作做完了')
    print('任务一继续')
@asyncio.coroutine
def hello2():
    print('任务二 开始了!')
    print('执行中')
    print('遇到了费时操作')
    r = yield from asyncio.sleep(5)
    print('任务二费事操作做完了')
    print('任务二继续')
start=datetime.datetime.now()
loop=asyncio.get_event_loop()
task = [hello(),hello2()]
loop.run_until_complete(asyncio.wait(task))
loop.close()
print(datetime.datetime.now()-start)