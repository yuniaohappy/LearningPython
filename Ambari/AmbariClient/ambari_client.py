from ambariclient.client import Ambari
import six

# print(help(Ambari))
# ambari = Ambari('172.20.10.11', port=8080, username='admin', password='admin')

# import json
# with open("E:\hive.json",'r') as f:
#     print(f.readlines())
#     j = json.loads(f.readlines())
#
#     print(json.dumps(j,indent=2))


# class Singleton(object):
#     __instance=None
#     def __init__(self):
#         pass
#     def __new__(cls,*args,**kwd):
#         if Singleton.__instance is None:
#         Singleton.__instance=object.__new__(cls,*args,**kwd)
#         return Singleton.__instance


class Foo:
    __v = None
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if Foo.__v is None:
            Foo.__v = object.__new__(cls, *args, **kwargs)
        return Foo.__v

    # def get_instance(self):
    #     if Foo.__v:
    #         return Foo.__v
    #     else:
    #         Foo.__v = Foo()
    #         return Foo.__v
obj1 = Foo()
print(obj1)
obj2 = Foo()
print(obj2)
obj3 = Foo()
print(obj3)