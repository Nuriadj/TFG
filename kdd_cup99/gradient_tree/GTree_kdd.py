#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import pandas as pd
from sklearn import metrics
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import matplotlib.pyplot as plt
from collections import Counter


# In[ ]:


dataset = pd.read_csv('/home/nuria/Documents/TFG/kdd_cup99/kddcup_10_perBinary.csv', header= None)
headers = list(dataset.columns.values)


# In[ ]:


#Eliminar datos Redundantes
dataset.drop(dataset.columns[19], axis= 1, inplace= True)
dataset.drop(dataset.columns[20], axis= 1, inplace= True)


# In[ ]:


#Las tres primeras columnas contienen strings

dataset[1] = dataset[1].astype('category')
dataset[2] = dataset[2].astype('category')
dataset[3] = dataset[3].astype('category')
cat_columns = dataset.select_dtypes(['category']).columns
dataset[cat_columns] = dataset[cat_columns].apply(lambda x: x.cat.codes)


# In[ ]:


#Eliminar duplicados
dataset.drop_duplicates(subset=None, keep='first', inplace=True)


# In[ ]:


x= dataset.iloc[:, :-1].values
y= dataset.iloc[:, 39].values


# In[ ]:


#-- 70% train 30% test y estratificado--
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.30, stratify=y)

scaler = preprocessing.StandardScaler().fit(x_train)
x_scaled = scaler.transform(x_train)

scaler = preprocessing.StandardScaler().fit(x_test)
x_test_scaled = scaler.transform(x_test)


# In[ ]:


gtb = GradientBoostingClassifier()
gtb.fit(x_scaled, y_train)
occup_pred = gtb.predict(x_test_scaled)


# In[ ]:


accuracy = metrics.accuracy_score(y_test, occup_pred)*100
print("Accuracy: ","{:.1f}".format(accuracy),"%")
precision = metrics.precision_score(y_test, occup_pred, pos_label='normal.')*100
print("Precision: ","{:.1f}".format(precision),"%")
recall = metrics.recall_score(y_test, occup_pred, pos_label='normal.')*100
print("Recall: ","{:.1f}".format(recall),"%")

