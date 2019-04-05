import tensorflow as tf
import numpy as np
import matplotlib.pylab as plb
import matplotlib.pyplot as plt

from pyhive import hive
conn = hive.Connection(host='localhost',port=10000,username='hive',database='ods_import').cursor()
res = conn.fetchall("select * from ods_import limit 10")
print(res)
