import sys
import traceback


try:
    x = int(input('请输入一个被除数：'))
    print('30 除以', x, '等于',30/x)
except :
    traceback.print_exc()
    # print(sys.exc_info())

# except Exception as e:
#     print(e)

# except (ValueError,ZeroDivisionError):
#     print('输入无效')
# # except ZeroDivisionError:
# #     print('被除数不能等于0')
# except:
#     print('其他异常。。。。')
# else:
#     print('Bye!!!')