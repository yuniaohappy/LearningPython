# 迭代器的实现原理
class Reverse:
    def __init__(self,datastr):
        self._data = datastr
        self._index = len(datastr)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index == 0:
            raise(StopIteration)
        self._index -= 1
        return self._data[self._index]

revstr = Reverse('lipeng')
for rev in revstr:
    print(rev,end=' ')

