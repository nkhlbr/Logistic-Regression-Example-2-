# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd 
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

ad_data = pd.read_csv('advertising.csv')

ad_data.info()  #info of columns

ad_data.describe() #statistical information

ad_data['Age'].plot.hist(bins=35) #HIstogram for Age

sns.jointplot(x='Age', y = 'Area Income', data=ad_data) #Create a jointplot for Area vs Age

sns.jointplot(x='Age', y = 'Daily Time Spent on Site', data=ad_data, kind='kde', color = 'Red')

sns.jointplot(x = 'Daily Time Spent on Site', y = 'Daily Internet Usage', data = ad_data)

sns.pairplot(ad_data, hue='Clicked on Ad')

#Visualising the data

from sklearn.model_selection import train_test_split

X = ad_data[['Daily Time Spent on Site',	'Age',	'Area Income',	'Daily Internet Usage',	'Male'	]]
y = ad_data['Clicked on Ad']

X_train,X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=101)

from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)

#Training the data


#Predicting and Evaluating the data

predictions = logmodel.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,predictions))
print(confusion_matrix(y_test,predictions))