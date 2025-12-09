from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes

import matplotlib.pyplot as plt

model = LinearRegression(custom_scaling=-1.5, copy_X=True)

X, y = load_diabetes(return_X_y=True)
print(X[0])

model.fit(X, y)
print(X[0])

pred = model.predict(X[:10])

plt.scatter(range(10), y[:10], color='green')
plt.scatter(range(10), pred, color='red')
plt.show()
