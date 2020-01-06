# 基于事件机制的消息队列
import queue
from random import randint
from threading import Thread
from threading import Event

class WriteThread(Thread):
    def __init__(self,q,WE,RE):
        super().__init__()
        self.queue = q
        self.RE = RE
        self.WE = WE

    def run(self):
        data = [randint(1,10) for _ in range(0,5)]
        self.queue.put(data)
        print('WriteThread 写队列：',data)
        self.RE.set()
        print('WriteThread 通知读事件')
        print('WriteThread 等待写事件')
        self.WE.wait()
        print('WriteThread 收到写事件')
        self.WE.clear()

class ReadThread(Thread):
    def __init__(self,q,WE,RE):
        super().__init__()
        self.queue = q
        self.RE = RE
        self.We = WE

    def run(self):
        while True:
            self.RE.wait()
            print('ReadThread 收到读事件')
            data = self.queue.get()
            print('ReadThread 读队列 {}'.format(data))
            print('ReadThread 发送写事件')
            self.We.set()
            self.RE.clear()

q = queue.Queue()
WE = Event()
RE = Event()
writethread = WriteThread(q,WE,RE)
readthread = ReadThread(q,WE,RE)
writethread.start()
readthread.start()

