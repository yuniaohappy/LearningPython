import logging
import math
import dicom
import os
import PIL.Image as Image

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(module)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger(__name__)

def load_scan(path):
    s = [dicom.read_file(os.path.join(path,s)) for s in os.listdir(path)]
    return s
path = 'E:\BaiduNetdiskDownload\python带我起飞书籍配套资料\资源\实例24\patient32\P32dicom'
patient = load_scan(path)
# log.info(patient[0])
# log.info(patient[0].dir())
# log.info(patient[0].dir('pat'))
# log.info(patient[0].PatientName)
#
# # 读取DICOM图像数据并展示
# import pylab
# pylab.imshow(patient[0].pixel_array,cmap=pylab.cm.bone)
# pylab.show()D

# 将DICOM生成到一张图片里
def plot_ct_scan(scan):
    length = len(scan)
    each_size = int(math.sqrt(float(810*810)/length))
    lines = int(810/each_size)
    image = Image.new('RGB',(810,810),'white')
    x = 0
    y = 0
    for i in range(0,length):
        img = Image.fromarray(scan[i].pixel_array.astype(int))
        img = img.resize((each_size,each_size),Image.ANTIALIAS)
        image.paste(img,(x * each_size,y * each_size))
        x += 1
        if x == lines:
            x = 0
            y += 1
    log.info('开始写入文件。。。')
    image.save('all.jpg')
    log.info('写入文件完成。。。')
plot_ct_scan(patient)

