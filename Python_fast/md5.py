import hashlib
import os
import datetime
import argparse


def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(80960)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()


# filepath = raw_input('请输入文件路径：')

ap = argparse.ArgumentParser(description='计算文件的MD5值')
ap.add_argument('--path', help='文件路径', default='G:\like\library.tar.gz')
args = ap.parse_args()

# 输出文件的md5值以及记录运行时间
starttime = datetime.datetime.now()
print(GetFileMd5(args.path))
endtime = datetime.datetime.now()
print('运行时间：%ds' % ((endtime - starttime).seconds))
