import logging
import logging.handlers
import logging.config


logger = logging.getLogger(__name__)
# 多装饰器的调用顺序
def logg(fn):
    logger.debug('in  logging')
    def wrapper_logging(*args,**kwargs):
        logger.debug('in wrapper_logging')
        return fn(*args,**kwargs)
    return wrapper_logging
def checkParams(fn):
    logger.debug('in checkParams')
    def wrapper_checkParams(*args,**kwargs):
        logger.debug('in wrapper_checkParams')
        return fn(*args,**kwargs)
    return wrapper_checkParams

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s %(processName)s '
                           '%(module)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

@logg
@checkParams
def wrapperfun(name):
    logger.debug('姓名：{}'.format(name))
wrapperfun('Anna')

#装饰器实现原理
# def checkParams(fn):
#     def wrapper(name):
#         if isinstance(name,str):
#             return fn(name)
#         print('参数类型不正确！！！')
#         return None
#     return wrapper
# @checkParams
# def wrapperfun(name):
#     def recoder(age):
#         logger.debug("姓名：%s 姓名：%s",name,age)
#     return recoder
# 第一种基本日志格式
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(name)s %(levelname)s %(processName)s '
#                            '%(module)s %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S')

# 第二中日志格式
# formatter = logging.Formatter(fmt='%(asctime)s %(name)s %(levelname)s %(processName)s '
#                                   '%(module)s %(message)s',
#                               datefmt='%Y-%m-%d %H:%M:%S')
# fh = logging.FileHandler('./test.log',encoding='utf-8')
# fh.setFormatter(formatter)
# sh = logging.StreamHandler()
# sh.setFormatter(formatter)
# logger.setLevel(logging.DEBUG)
# logger.addHandler(sh)
# logger.addHandler(fh)
# logging.Handler()

# wrapperfun2 = checkParams(wrapperfun)
# fun = wrapperfun2('Anna')
# fun(37)
# logger.debug('测试日志001')
# logger.debug('测试日志002')
# fun = wrapperfun('Anna')
# fun(37)
# fun = wrapperfun(37)

# sh.close()
# fh.close()





#闭包的实现过程
# def recoder(name,age):
#     print('姓名：',name,'年龄：',age)
# def Garyfun(age):
#     name = 'Gary'
#     return recoder(name,age)
# Garyfun(32)
# def Annafun(age):
#     name = 'Anna'
#     return recoder(name,age)
# Annafun(20)
#
# def wrapperfun(name):
#     def recoder(age):
#         print('姓名：',name,'年龄：',age)
#     return recoder
# fun = wrapperfun('Gary')
# print(fun.__closure__)
# fun(32)
#
# fun1 = wrapperfun('Anna')
# fun1(20)
