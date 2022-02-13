#!/usr/bin/env python
# coding: utf-8

# In[13]:


import csv
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier


# In[14]:


dataset = pd.read_csv('/home/nuria/Documents/Occupancy/Occupancy.csv', header= 0)
headers = list(dataset.columns.values)


# In[15]:


x= dataset.drop(['Occupancy', 'date'], axis= 1).values#quitar occupancy y date
y= dataset['Occupancy'].values#la salida


# In[16]:


#-- 70% train 30% test y estratificado--
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.3, stratify=y)


# In[17]:


get_ipython().run_cell_magic('time', '', 'gtb = GradientBoostingClassifier()\ngtb.fit(x_train, y_train)\noccup_pred = gtb.predict(x_test)')


# In[18]:


accuracy = metrics.accuracy_score(y_test, occup_pred)*100
print("Accuracy: ","{:.1f}".format(accuracy),"%")
precision = metrics.precision_score(y_test, occup_pred)*100
print("Precision: ","{:.1f}".format(precision),"%")
recall = metrics.recall_score(y_test, occup_pred)*100
print("Recall: ","{:.1f}".format(recall),"%")

