"""进程lock"""
# import multiprocessing as mp
# import time
#
# def job(v, num, l):
#     l.acquire()
#     for _ in range(10):
#         time.sleep(0.1)
#         v.value += num
#         print(v.value)
#     l.release()
#
# def multicore():
#     l = mp.Lock()
#     v = mp.Value('i', 0)
#     p1 = mp.Process(target=job, args=(v, 1, l))
#     p2 = mp.Process(target=job, args=(v, 3, l))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#
# if __name__ == '__main__':
#     multicore()

"""共享内存"""
# import multiprocessing as mp
# value = mp.Value('d', 0)
# array = mp.Array('a',[2,3,4,5])

"""Pool线程池"""
# import multiprocessing as mp
#
# def job(x):
#     return x*x
#
# def multicore():
#     pool = mp.Pool(processes=3)
#     res = pool.map(job, range(10))
#     print(res)
#     res1 = pool.apply_async(job, (2,))
#     print(res1.get())
#     print([x.get() for x in [pool.apply_async(job, (x,)) for x in range(10)]])
#     # print([i.get() for i in res2])
#
# if __name__ == "__main__":
#     multicore()

"""Threading和Processing效率对比"""
# import multiprocessing as mp
# import threading as th
# import time
#
# def job(q):
#     res = 0
#     for i in range(1000000):
#         res += i + i**2 + i**3
#     q.put(res)
#
# def multicore():
#     q = mp.Queue()
#     p1 = mp.Process(target=job, args=(q,))
#     p2 = mp.Process(target=job, args=(q,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     res1 = q.get()
#     res2 = q.get()
#     print("multiCore: ", res1 + res2)
#
# def normal():
#     res = 0
#     for _ in range(2):
#         for i in range(1000000):
#             res += i + i ** 2 + i ** 3
#
#     print("normal", res)
#
# def multithread():
#     q = mp.Queue()
#     t1 = th.Thread(target=job, args=(q,))
#     t2 = th.Thread(target=job, args=(q,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     res1 = q.get()
#     res2 = q.get()
#     print("multithread: " , res1 + res2)
#
# if __name__ == '__main__':
#     st = time.time()
#     normal()
#     st1 = time.time()
#     print("normal time: " , st1 - st)
#     multithread()
#     stm = time.time()
#     print("multithread time: ", stm - st1)
#     multicore()
#     stc = time.time()
#     print("multicore time: ", stc - stm)

"""Queue进程输出"""
# import multiprocessing as mp
# def job(q):
#     print("aaa")
#     res = 0
#     for i in range(1000):
#         res += i + i**2 + i**3
#     q.put(res)
#
# if __name__ == '__main__':
#     q = mp.Queue()
#     p1 = mp.Process(target=job,args=(q,))
#     p2 = mp.Process(target=job,args=(q,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     res1 = q.get()
#     res2 = q.get()
#     print(res1)
#     print(res2)
#     print(res1 + res2)

"""Processing"""
# import multiprocessing as mp
# # import threading as td
#
# def job(a, b):
#     print("aaa")
#     print( a + b)
#
# # t1 = td.Thread(target=job,args=(1,2))
# if __name__ == '__main__':
#     p1 = mp.Process(target=job,args=(1,2))
# # t1.start()
#     p1.start()
# # t1.join()
#     p1.join()