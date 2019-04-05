from multiprocessing import Process,Queue

def f(q):
    q.put([42,2,'hello'])
    print("subprocess:",id(q))

if __name__ == '__main__':
    q = Queue()
    p_list = []
    print('main:', id(q))
    for i in range(3):
        p = Process(target=f,args=(q,))
        p_list.append(p)
        p.start()

    print(q.get())
    print(q.get())
    print(q.get())

    for i in p_list:
        i.join()
