#!/usr/bin/env python
# coding: utf-8

# In[17]:


import csv
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import StratifiedKFold, KFold


# In[18]:


dataset = pd.read_csv('/home/nuria/Documents/Occupancy/Occupancy.csv', header= 0)
headers = list(dataset.columns.values)


# In[19]:


x= dataset.drop(['Occupancy', 'date'], axis= 1).values#quitar occupancy y date
y= dataset['Occupancy'].values#la salida


# In[20]:


#-- 70% train 30% test y estratificado--
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.3, stratify=y)


# In[21]:


skf = StratifiedKFold(n_splits= 5)
#skf = KFold(n_splits= 5)
gtb = GradientBoostingClassifier()

acc_score= []
prec_score= []
rec_score= []


# In[22]:


for train_index, test_index in skf.split(x_train, y_train):
    x_subtrain, x_subtest = x_train[train_index,:], x_train[test_index,:]
    y_subtrain, y_subtest = y_train[train_index], y_train[test_index]
    
    gtb.fit(x_subtrain, y_subtrain)
    
    pred_values = gtb.predict(x_subtest)
    
    acc = metrics.accuracy_score(y_subtest, pred_values)*100
    acc_score.append("{:.1f}".format(acc)+"%")
    prec = metrics.precision_score(y_subtest, pred_values)*100
    prec_score.append("{:.1f}".format(prec)+"%")
    rec = metrics.recall_score(y_subtest, pred_values)*100
    rec_score.append("{:.1f}".format(rec)+"%")


# In[23]:


print('Accuracy of each fold', acc_score)
print('Precision of each fold', prec_score)
print('Recall of each fold', rec_score)


# In[24]:


occup_pred = gtb.predict(x_test)

accuracy= metrics.accuracy_score(y_test, occup_pred)*100
print("Accuracy {:.1f}".format(accuracy),"%")
precision = metrics.precision_score(y_test, occup_pred)*100
print("Precision: ","{:.1f}".format(precision),"%")
recall = metrics.recall_score(y_test, occup_pred)*100
print("Recall: ","{:.1f}".format(recall),"%")

