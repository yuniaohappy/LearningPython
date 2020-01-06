# 使用信号量来同步多线程间的顺序关系
import threading
import time
import random

# semaphore = threading.Semaphore(0)
semaphore = threading.BoundedSemaphore(1)
item = 0
def consumer():
    print('Consumer: 挂起。。。')
    semaphore.acquire()
    print('consumer: 消费 {}'.format(item))

def producer():
    global item
    time.sleep(3)
    item = random.randint(1,1000)
    print('producer : 生产 {}'.format(item))
    semaphore.release()

threads = []
for i in range(0,2):
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()
    threads.append(t1)
    threads.append(t2)

for t in threads:
    t.join()

