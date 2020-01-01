#断言assert
import traceback

try:
    assert 1 != 1,('1不等于1，报错')
except AssertionError:
    # traceback.print_exc()
    print('出异常了')