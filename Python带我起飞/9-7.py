# class ChainURL(object):
#     def __init__(self,attr=''):
#         self._data = attr
#
#     def __getattr__(self, item):
#         return ChainURL('%s/%s' % (self._data,item))
#
#     def __str__(self):
#         return self._data
#
#     __repr__ = __str__
#
# print(ChainURL().status.alluser.list)

class ChainURL(object):
    def __init__(self,attr=''):
        self._data = attr

    def __getattr__(self, item):
        return ChainURL('{}/{}'.format(self._data,item))

    def __call__(self, attr):
        return ChainURL('{}/{}'.format(self._data,attr))

    def __str__(self):
        return self._data
    __repr__ = __str__

print(ChainURL().users('Anna').info)

