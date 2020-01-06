# 条件锁的应用

from threading import Thread
from threading import Condition
import time
import random

c = Condition()
itemNum = 0
item = 0

def consumer():
    global  item
    global itemNum
    c.acquire()
    while 0 == itemNum:
        print('consumer: 挂起。。。')
        c.wait()
    itemNum -= 1
    print('consumer: 消费 {}'.format(item),itemNum)
    c.release()

def producer():
    global  item
    global itemNum
    time.sleep(3)
    c.acquire()
    item = random.randint(1,1000)
    itemNum += 1
    print('producer : 生产 {}'.format(item))
    c.notifyAll()
    c.release()

threads = []
for i in range(0,2):
    t1 = Thread(target=producer)
    t2 = Thread(target=consumer)
    t1.start()
    t2.start()
    threads.append(t1)
    threads.append(t2)

for t in threads:
    t.join()
