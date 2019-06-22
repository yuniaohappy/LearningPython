import numpy as np
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
# >>> import numpy as np
# >>> from sklearn import metrics
# >>> y = np.array([1, 1, 2, 2])
# >>> scores = np.array([0.1, 0.4, 0.35, 0.8])
# >>> fpr, tpr, thresholds = metrics.roc_curve(y, scores, pos_label=2)
# >>> fpr
# array([ 0. ,  0.5,  0.5,  1. ])
# >>> tpr
# array([ 0.5,  0.5,  1. ,  1. ])
# >>> thresholds
# array([ 0.8 ,  0.4 ,  0.35,  0.1 ])
y = np.array([1,1,2,2])
scores = np.array([0.1,0.4,0.35,0.8])
fpr,tpr,thresholds = roc_curve(y,scores,pos_label=2)
print(fpr)
print(tpr)
print(thresholds)
plt.plot(fpr,tpr)
plt.show()
