import platform
import os
import sys
# yu = __import__("9-24 yuyinutils")

def showENV():
    s = platform.platform()
    print("当前系统：",s)
    # print(platform.version())
    # print(platform.release())

    p = sys.path
    print("当前安装路径：",p)
    print(sys.platform,sys.version)

    op = os.getcwd()
    print(op)

    print(sys.version_info)

if __name__ == "__main__":
    showENV()