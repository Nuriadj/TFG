#!/usr/bin/env python
# coding: utf-8

# In[439]:


import csv
import pandas as pd
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


# In[440]:


dataset = pd.read_csv('/home/nuria/Documents/Occupancy/Occupancy.csv', header= 0)
headers = list(dataset.columns.values)


# In[441]:


x= dataset.drop(['Occupancy', 'date'], axis= 1).values#quitar occupancy y date
y= dataset['Occupancy'].values#la salida


# In[442]:


#-- 70% train 30% test y estratificado--
x_train, x_test, y_train, y_test = train_test_split(x,y, train_size= 0.70, stratify=y)


# In[443]:


get_ipython().run_cell_magic('time', '', 'l_regr= LogisticRegression()\n# Entrenamiento\nl_regr.fit(x_train, y_train)\n# Prediccion\noccup_pred = l_regr.predict(x_test)')


# In[444]:


accuracy = metrics.accuracy_score(y_test, occup_pred)*100
print("Accuracy: ","{:.1f}".format(accuracy),"%")
precision = metrics.precision_score(y_test, occup_pred)*100
print("Precision: ","{:.1f}".format(precision),"%")
recall = metrics.recall_score(y_test, occup_pred)*100
print("Recall: ","{:.1f}".format(recall),"%")


# In[445]:


cm= confusion_matrix(y_test, occup_pred)

fig, ax= plt.subplots(figsize=(2,2))
ax.imshow(cm)
ax.grid(False)
ax.set_xlabel('Predicted outputs')
ax.set_ylabel('Actual outputs')
for i in range(2):
    for j in range(2):
        ax.text(j,i,cm[i,j],ha='center', va='center',color='white')
plt.show()

