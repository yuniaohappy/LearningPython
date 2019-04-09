import time
import threading

class MyThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num
    def run(self):
        print("running on number:%s" % self.num)
        time.sleep(3)

t1 = MyThread(2)
t2 = MyThread(3)
t1.start()
t2.start()