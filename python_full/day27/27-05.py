import time
import threading
start = time.time()

def foo(n):
    print("foo%s" % n)
    time.sleep(1)
    print("foo end")

def bar(n):
    print("bar%s"%n)
    time.sleep(2)
    print("bar end")

# foo()
# bar()
t1 = threading.Thread(target=foo,args=(2,))
t2 = threading.Thread(target=bar,args=(3,))
t1.start()
t2.start()
print("...........star.............")
t1.join()
t2.join()
end = time.time()
print(end - start)
