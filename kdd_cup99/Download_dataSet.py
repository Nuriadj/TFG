#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sklearn
from sklearn import datasets
import pandas as pd
import numpy
import random


# In[2]:


#data= sklearn.datasets.fetch_kddcup99(data_home="/home/nuria/Documents/TFG/sklearnDataSet", percent10=True, as_frame= True)
#print(data)


# In[ ]:


n= 4940200 # 494020 es el 10% del total, luego el fichero total tendra 4940200 lineas
s= 2470100 # Leer solo el 50%
skip= sorted(random.sample(range(n),n-s))
dataset = pd.read_csv('/home/nuriadj/Documents/TFG/kdd_cup99/kddcup.data', skiprows=skip)
print("Leido un: ",(len(dataset)*100)/n,"% del csv")
headers = list(dataset.columns.values)

#dataset= pd.read_csv('/home/nuriadj/Documents/TFG/kdd_cup99/kddcup.data')

#change Multi-class to binary-class
dataset['normal.'] = dataset['normal.'].replace(['back.', 'buffer_overflow.', 'ftp_write.', 'guess_passwd.', 'imap.', 'ipsweep.', 'land.', 'loadmodule.', 'multihop.', 'neptune.', 'nmap.', 'perl.', 'phf.', 'pod.', 'portsweep.', 'rootkit.', 'satan.', 'smurf.', 'spy.', 'teardrop.', 'warezclient.', 'warezmaster.'], 'attack')

dataset.to_csv('kddcup_50_perBinary.csv', header= False, index= False)

