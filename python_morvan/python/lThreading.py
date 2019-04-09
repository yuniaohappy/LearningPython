"""线程锁Lock"""
import threading


def job1():
    global A
    lock.acquire()
    for i in range(10):
        A += 1
        print("job1: ", A)
    lock.release()


def job2():
    global A
    lock.acquire()
    for i in range(10):
        A += 10
        print("job2: ", A)
    lock.release()

    
if __name__ == '__main__':
    lock = threading.Lock()
    A = 0
    th1 = threading.Thread(target=job1)
    th2 = threading.Thread(target=job2)
    th1.start()
    th2.start()
    th1.join()
    th2.join()

"""GIL不一定有效率"""
# import threading
# from queue import Queue
# import copy
# import time
#
# def job(l, q):
#     res = sum(l)
#     q.put(res)
# def multithreading(l):
#     q = Queue()
#     threads = []
#     for i in range(4):
#         t = threading.Thread(target=job, args=(copy.copy(l), q),name="T %s" % i)
#         t.start()
#         threads.append(t)
#     [thread.join() for thread in threads]
#
#     results = 0
#     for _ in range(4):
#         results += q.get()
#     print("multithreading sum : ", results)
#
# def normal(l):
#     res = sum(l)
#     print("normal sum : " , res)
#
# if __name__ == '__main__':
#     l = list(range(1000000))
#     st = time.time()
#     normal(l * 4)
#     stn = time.time()
#     print("normal time: ",stn - st)
#     multithreading(l)
#     stm = time.time()
#     print("multithreading time: ", stm - stn)

"""join功能"""
# import threading
# import time
# def thread_job():
#     print("T1 start\n")
#     for i in range(10):
#         time.sleep(0.1)
#     print("T1 finish\n")
# def T2_job():
#     print("T2 start\n")
#     print("T2 finish\n")
#
# def main():
#     added_thread = threading.Thread(target=thread_job,name="T1")
#     thread2 = threading.Thread(target=T2_job(),name="T2")
#     added_thread.start()
#     thread2.start()
#     added_thread.join()
#     thread2.join()
#     print("all done\n")
#
# if __name__ == '__main__':
#     main()

"""存储进程结果Queue"""
# import threading
#
# from queue import Queue
# def job(l, q):
#     for i in range(len(l)):
#         l[i] = l[i]**2
#     q.put(l)
# def multireading():
#     q = Queue()
#     threads = []
#     data = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]
#     for i in range(4):
#         t = threading.Thread(target=job, args=(data[i], q))
#         t.start()
#         threads.append(t)
#     for thread in threads:
#         thread.join()
#     results = []
#     for _ in range(4):
#         results.append(q.get())
#     print(results)
#
# if __name__ == '__main__':
#     multireading()

"""join功能"""
# import threading
# import time
# def thread_job():
#     print("T1 start\n")
#     for i in range(10):
#         time.sleep(0.1)
#     print("T1 finish\n")
# def T2_job():
#     print("T2 start\n")
#     print("T2 finish\n")
#
# def main():
#     added_thread = threading.Thread(target=thread_job,name="T1")
#     thread2 = threading.Thread(target=T2_job(),name="T2")
#     added_thread.start()
#     thread2.start()
#     added_thread.join()
#     thread2.join()
#     print("all done\n")
#
# if __name__ == '__main__':
#     main()

"""添加线程Threading"""
# import threading
# def thread_job():
#     print("This is an added Thread,number is %s" % threading.current_thread())
#
# def main():
#     added_thread = threading.Thread(target=thread_job)
#     added_thread.start()
#     print(threading.active_count())
#     print(threading.enumerate())
#     print(threading.current_thread())
#
# if __name__ == '__main__':
#     main()