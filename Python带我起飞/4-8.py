from collections import deque
queue = deque()

queue.append(1)
queue.append(2)
queue.append('hellp')

print(list(queue))
# print(queue.popleft())
# print(queue.popleft())
print(queue.pop())
print(queue.pop())
print(queue)



# queue = []

# 使用list实现队列
# queue.insert(0,1)
# queue.insert(0,2)
# queue.insert(0,'hello')
# print(queue)
#
# print('第一个元素：',queue.pop())
# print('第二个元素：',queue.pop())
# print('第三个元素：',queue.pop())
#
# queue.append(1)
# queue.append(2)
# queue.append('hello')
# print(queue)
# print('第一个元素：',queue.pop(0))
# print('第二个元素：',queue.pop(0))
# print('第三个元素：',queue.pop(0))

# 使用list实现栈
# queue.append(1)
# queue.append(2)
# queue.append('hello')
# print(queue)
# print('第一个元素：',queue.pop())
# print('第二个元素：',queue.pop())
# print('第三个元素：',queue.pop())