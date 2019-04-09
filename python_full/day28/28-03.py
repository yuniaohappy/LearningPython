import threading,time

class MyThread(threading.Thread):
    def doA(self):
        lock.acquire()
        print(self.name,"gotLockA",time.ctime())
        time.sleep(3)
        lock.acquire()
        print(self.name,"gotLockB",time.ctime())
        lock.release()
        lock.release()
    def doB(self):
        lock.acquire()
        print(self.name, "gotLockB", time.ctime())
        time.sleep(3)
        lock.acquire()
        print(self.name, "gotLockA", time.ctime())
        lock.rel,n, base()
        lock.release()
    def run(self):
        self.doA()
        self.doB()

if __name__ == "__main__":
    # lockA = threading.Lock()
    # lockB = threading.Lock()
    lock = threading.RLock()
    mythreads = []
    for i in range(5):
        mythreads.append(MyThread())
    for t in mythreads:
        t.start()
    for t in mythreads:
        t.join()