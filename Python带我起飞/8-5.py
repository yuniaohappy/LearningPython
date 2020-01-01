# b1 = b'lipeng'
# b2 = bytes('lipeng','utf-8')
# print(b1,b2)
# print(b2,b2.decode())

import pickle
import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(name)s %(levelname)s %(processName)s '
#                            '%(module)s %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)s %(levelname)s %(module)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger(__name__)
t1 = ('I Love Python',[1,2,2],None)
file = 'a.pkl'
# p1 = pickle.dumps(t1)
# # print(p1)
# # t2 = pickle.loads(p1)
# # print(t2)
with open(file,'wb') as f:
    pickle.dump(t1,f,pickle.HIGHEST_PROTOCOL)
    log.info('文件生成成功！！！')

with open(file,'rb') as f:
    f1 = pickle.load(f)
    log.info(f1)


