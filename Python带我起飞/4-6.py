"""
序列类型的基本操作
"""

s = 'hello'
s2 = 'daimayisheng'

print(s + s2)
print(s * 3)
print(s[0],s[2])
print(s.index('e'))

import gc
gc.collect()
