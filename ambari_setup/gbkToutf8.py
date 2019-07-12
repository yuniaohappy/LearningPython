import codecs


def readFile(filePath,encoding='gbk'):
    with codecs.open(filePath,'r',encoding,errors='ignore') as f:
        return f.read()

def writeFile(filePath,file,encoding='utf8'):
    with codecs.open(filePath,'w',encoding,errors='ignore') as f:
        return f.write(file)

def gbk2utf8(src,dst):
    tran = readFile(src)
    writeFile(dst,tran)

if __name__ == '__main__':
    # codecs.EncodedFile('./test_gbk01.txt','gbk',file_encoding='utf8')
    gbk2utf8('./test_gbk.txt','./test_utf8.txt')

