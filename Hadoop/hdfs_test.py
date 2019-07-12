import pyhdfs
import os
import shutil
import sys

fs = pyhdfs.HdfsClient('20.200.56.229:50070',user_name='hdfs')

def creat_fs(path):
    if path is not None:
        # fs.create(path,)
        fs.mkdirs(path)
    else:
        print('path is None')

def delete_fs(path):
    if fs.exists(path):
        fs.delete(path)
    else:
        print('path is None,delete error')

# FileStatus(accessTime=0,
# blockSize=0,
# childrenNum=6,
# fileId=16392,
# group='hadoop',
# length=0,
# modificationTime=1553755334860,
# owner='yarn',
# pathSuffix='app-logs',
# permission='777',
# replication=0,
# storagePolicy=0,
# type='DIRECTORY')

def trim_dir(path):
    if fs.exists(path):
        fst = fs.list_status(path)
        for f in fst:
            if f.type == 'DIRECTORY':
                if f.childrenNum == 0:
                    print(path + '/' + f.pathSuffix)
                else:
                    trim_dir(path + '/' + f.pathSuffix)
    else:
        print(path,'路径不存在')

def download_file(srcPath,destPath):
    # if not os.path.exists(destPath):
    #     print('目录不存在，创建目录。。。')
    #     os.mkdir(destPath)
    if fs.exists(srcPath):
        fs.copy_to_local(srcPath,destPath)
    else:
        print("文件不存在")



if __name__ == '__main__':
    # # creat_fs('/lipeng')
    # delete_fs('/lipeng')
    # print(fs.listdir('/'))
    # trim_dir('/apps')
    download_file('/tmp/java-1.7.0-openjdk-1.7.0.141-2.6.10.5.el7.x86_64.rpm','./lipeng/java-1.7.0-openjdk-1.7.0.141-2.6.10.5.el7.x86_64.rpm')