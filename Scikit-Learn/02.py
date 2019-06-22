from sklearn.datasets import load_iris
from sklearn.linear_model.logistic import LogisticRegression
import pandas as pd
import matplotlib.pyplot as plt
iris = load_iris()
x,y = iris.data,iris.target
# df = pd.DataFrame(x)

# print(df.values)
print(x[:,:1])
plt.hist(x[:,:1])
plt.show()

