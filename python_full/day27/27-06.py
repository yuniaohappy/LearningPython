import time
import threading
start = time.time()

def add(n):
    sum = 0
    for i in range(n):
        sum += i
    print(sum)

# add(1000000000)
# add(1000000000)
t1 = threading.Thread(target=add,args=(100000000,))
t1.start()
t2 = threading.Thread(target=add,args=(100000000,))
t2.start()
t1.join()
t2.join()
end = time.time()
print(end - start)