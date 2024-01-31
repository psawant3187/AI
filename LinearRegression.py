import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes()

# (['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module']) 

# print(diabetes.keys()) To check all the keys associated with the dataset.

diabetes_X = diabetes.data # : = All elements , np.newaxis = To create new array of arrays , 2 = no.of elements in arrays/index.

# print(diabetes_X)

diabetes_X_train = diabetes_X[:-30] # Slicing last 30 elements of the datasets.
diabetes_X_test = diabetes_X[-20:] # Slicing first 20 elements of the datasets.

diabetes_Y_train = diabetes.target[:-30]
diabetes_Y_test = diabetes.target[-20:]

model = linear_model.LinearRegression()

model.fit(diabetes_X_train,diabetes_Y_train)

diabetes_Y_predict = model.predict(diabetes_X_test)

print("Mean Squared Error is:",mean_squared_error(diabetes_Y_test,diabetes_Y_predict))

print("Weights:",model.coef_)

print("Intercept:",model.intercept_)

# plt.scatter(diabetes_X_test,diabetes_Y_test)
# plt.plot(diabetes_X_test,diabetes_Y_predict)

# plt.show()

# Mean Squared Error is: 2561.320427728385
# Weights: [941.43097333]
# Intercept: 153.39713623331644