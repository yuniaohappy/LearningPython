import traceback

try:
    x = int(input('请输入一个被除数：'))
    if x == 0:
        raise ValueError('被除数不能为0！！！')
    print('30除以 ',x,'等于',30/x)
# except Exception as e:
#     print(e)
except ValueError:
    traceback.print_exc()
else:
    print('计算完毕！！！')
finally:
    print('123')