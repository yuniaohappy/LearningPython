import traceback

class DatalabError(Exception):
    pass

try:
    print('open file')
    print('读取内容')
    # raise IOError('读取出错')
    raise DatalabError('数据出错！！！')
except DatalabError:
    traceback.print_exc()
# except Exception as e:
#     print(e)
    # traceback.print_exc()
finally:
    print('关闭文件')