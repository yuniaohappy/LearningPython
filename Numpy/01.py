import numpy as np
import time

test1 = 0
test2 = 0
start_time1 = time.time()
for i in range(1,1000000,1):
    test1 += i
time1 = time.time() - start_time1
print("Python 用时：" + str(time1),test1)
# Python 用时：0.013989448547363281 4999950000
# Numpy 用时：0.015624523162841797 4999950000

start_time2 = time.time()
for x in np.array(np.arange(1,1000000,1),dtype='int64'):
    test2 += x
time2 = time.time() - start_time2
print("Numpy 用时：" + str(time2),test2)

# a = np.array([1.1,1.2,1.3,1.4,1.5])
# b = np.array([2.1,2.2,2.3,2.4,2.5])
# c = np.array([False,True,True,True,False])
# m =[x if z else y for x,y,z in zip(a,b,c)]
# print(m)

# nu = np.arange(15).reshape(3,5)
# # print(type(nu))
# print(nu)
# # print(nu[:1,1:3])
# # print(nu.T)
# print(np.dot(nu.T,nu))
