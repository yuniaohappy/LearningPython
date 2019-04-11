# yield实现协程
import time
import queue
def consumer(name):
    print("====starting====")
    while True:
        new_baozi = yield
        print("%s is eating baozi %s" % (name,new_baozi))

def producer():
    con.__next__()
    con.__next__()
    n = 0
    while n < 5:
        n += 1
        con.send(n)
        con2.send(n)
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)

if __name__ == "__main__":
    con = consumer('c1')
    con2 = consumer('c2')
    p = producer()