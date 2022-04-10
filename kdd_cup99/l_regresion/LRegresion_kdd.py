#!/usr/bin/env python
# coding: utf-8

# In[254]:

from time import time
import csv
import pandas as pd
import random
from sklearn import metrics
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from collections import Counter


# In[255]:

start= time()


n= 145584 # número de lineas limpias del 10% del fichero total
s= 145584 # Leer solo el 100%
skip= sorted(random.sample(range(n),n-s))
dataset = pd.read_csv('/home/nuriadj/Documents/TFG/kdd_cup99/kddcup_10_perClean.csv', header= None, skiprows=skip)
print("Leido un: ",(len(dataset)*100)/n,"% del csv")
headers = list(dataset.columns.values)
#print(headers)")


x= dataset.iloc[:, :-1].values
y= dataset.iloc[:, 39].values


# In[261]:


#-- 70% train 30% test y estratificado--
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.30, stratify=y)
scaler = preprocessing.StandardScaler().fit(x_train)
x_scaled = scaler.transform(x_train)
scaler = preprocessing.StandardScaler().fit(x_test)
x_test_scaled = scaler.transform(x_test)


# In[262]:

l_regr= LogisticRegression(max_iter= 400, n_jobs= 1)
# Entrenamiento
l_regr.fit(x_scaled, y_train)
# Prediccion
occup_pred = l_regr.predict(x_test_scaled)


# In[263]:


accuracy = metrics.accuracy_score(y_test, occup_pred)*100
print("Accuracy: ","{:.1f}".format(accuracy),"%")
precision = metrics.precision_score(y_test, occup_pred, pos_label='normal.')*100
print("Precision: ","{:.1f}".format(precision),"%")
recall = metrics.recall_score(y_test, occup_pred, pos_label='normal.')*100
print("Recall: ","{:.1f}".format(recall),"%")


end= time()
t_time= end-start

print("Total time: ",t_time)

# In[264]:


"""cm= confusion_matrix(y_test, occup_pred)

fig, ax= plt.subplots(figsize=(2,2))
ax.imshow(cm)
ax.grid(False)
ax.set_xlabel('Predicted outputs')
ax.set_ylabel('Actual outputs')
for i in range(2):
    for j in range(2):
        ax.text(j,i,cm[i,j],ha='center', va='center',color='white')
plt.show()"""

