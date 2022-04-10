#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import pandas as pd
import random
from sklearn import metrics
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from collections import Counter


# In[ ]:


n= 145584
s= 145584 # Leer solo el 10%
skip= sorted(random.sample(range(n),n-s))
dataset = pd.read_csv('/home/nuriadj/Documents/TFG/kdd_cup99/kddcup_10_perClean.csv', header= None, skiprows=skip)
print("Leido un: ",(len(dataset)*100)/n,"% del csv")
headers = list(dataset.columns.values)

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


r_forest= RandomForestClassifier(n_jobs= 8)
r_forest.fit(x_scaled, y_train)
occup_pred = r_forest.predict(x_test_scaled)


# In[ ]:


accuracy = metrics.accuracy_score(y_test, occup_pred)*100
print("Accuracy: ","{:.1f}".format(accuracy),"%")
precision = metrics.precision_score(y_test, occup_pred, pos_label='normal.')*100
print("Precision: ","{:.1f}".format(precision),"%")
recall = metrics.recall_score(y_test, occup_pred, pos_label='normal.')*100
print("Recall: ","{:.1f}".format(recall),"%")

