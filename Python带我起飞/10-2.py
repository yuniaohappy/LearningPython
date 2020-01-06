import threading
import time

# print(threading.current_thread())
# print(threading.enumerate())
# print(threading.active_count())
# print(len(threading.enumerate()))

# def handle(sid):
#     print('该线程的ID为：',sid,threading.current_thread())
# 创建10个线程
# for i in range(1,11):
#     t = threading.Thread(target=handle,args=(i,))
#     t.start()
# print('main thread ',threading.current_thread())

# 使用类继承的方式，并重载run方法
# class MyThread(threading.Thread):
#     def __init__(self,sid):
#         threading.Thread.__init__(self)
#         self.sid = sid
# #重写run方法
#     def run(self):
#         handle(self.sid)
#
# for i in range(1,11):
#     t = MyThread(i)
#     t.start()

# 线程中的互斥锁演示
g_num = 1
lock = threading.RLock()
def handle(sid):
    lock.acquire()
    global g_num
    g_num *= 2
    time.sleep(sid % 2)
    print('Thread ',sid,':',g_num)
    lock.release()

threads = []
for i in range(1,11):
    t = threading.Thread(target=handle,args=(i,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
print('main thread end')
