# -*- coding: utf-8 -*-
"""Lab3_FIA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O2hN7VsDfgSJBvYFnMGdz6-5D7X8IYHm
"""


import pandas 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset_path = 'https://raw.githubusercontent.com/speianudana/FIA/main/Lab3/apartmentComplexData.txt'
columns = ['col1', 'col2', 'complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr', 'col8', 'medianCompexValue']

dataset = pandas.read_csv(dataset_path, names=columns)
dataset.describe()


X = dataset[['col8']]
y = dataset['medianCompexValue'].values.flatten()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

reg = LinearRegression().fit(X_train, y_train)

print("Predict price on first row:")
print([X_test.iloc[0]])
print("Real price:", y_test[0])
prediction = reg.predict([X_test.iloc[0]])[0]
print("Predicted price:", prediction)
print("Difference:", abs(prediction-y_test[0]))
print("Difference in %: ", abs(prediction-y_test[0]) / y_test[0], "%")


X = dataset[['col1', 'col2', 'complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr', 'col8']]
y = dataset['medianCompexValue'].values.flatten()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

reg = LinearRegression().fit(X_train, y_train)

print("Predict price on first row of the X_test:")
print([X_test.iloc[0]])
print("Real price:", y_test[0])
prediction = reg.predict([X_test.iloc[0]])[0]
print("Predicted price:", prediction)
print("Difference:", abs(prediction-y_test[0]))
print("Difference in %: ", abs(prediction-y_test[0]) / y_test[0], "%")