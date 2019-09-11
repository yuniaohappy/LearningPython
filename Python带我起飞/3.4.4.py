import time

# print(time.__name__)
# print(time.__doc__)
# print(time.__package__)
# print(time.__loader__)
# print(time.__spec__)
print(time.time())
print(time.localtime().tm_hour)
print(time.ctime(1234569899))
print(time.ctime())
print(time.strptime('20190918','yyyy-mm-dd'))