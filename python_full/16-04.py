import time

def logger(flag=''):
    def show_time(func):
        def wrapper(*x):
            start_time = time.time()
            print('Start_time !!!')
            func(*x)
            end_time = time.time()
            print('End_time !!!')
            print('Spend %s' % (end_time - start_time))
            if flag == True:
                print('日志记录！！！')

        return wrapper
    return show_time
@logger()
def add(*a):
    su = sum(a)
    # for i in a:
    #     su += i
    print(su)

add(2,3,4,5)

# # @show_time
# def foo():
#     print('Hello foo !!!')
#     time.sleep(3)
#
# foo = show_time(foo)
#
# foo()