import numpy as np
import tensorflow as tf

seed = 2
def generateds():
    rdm = np.random.RandomState(seed)
    X = rdm.randn(300,2)
    Y_ = [int(x1*x1 + x2*x2 < 2) for (x1,x2) in X]

    Y_c = [['red' if y else 'blue'] for y in Y_]
    X = np.vstack(X).reshape(-1,2)
    Y_ = np.vstack(Y_).reshape(-1,1)

    return X,Y_,Y_c

