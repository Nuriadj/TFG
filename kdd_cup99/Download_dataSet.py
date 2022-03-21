#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sklearn
from sklearn import datasets
import pandas as pd
import numpy


# In[2]:


#data= sklearn.datasets.fetch_kddcup99(data_home="/home/nuria/Documents/TFG/sklearnDataSet", percent10=True, as_frame= True)
#print(data)


# In[ ]:


dataset= pd.read_csv('/home/nuria/Documents/TFG/sklearnDataSet/kddcup.csv')

#change Multi-class to binary-class
dataset['normal.'] = dataset['normal.'].replace(['back.', 'buffer_overflow.', 'ftp_write.', 'guess_passwd.', 'imap.', 'ipsweep.', 'land.', 'loadmodule.', 'multihop.', 'neptune.', 'nmap.', 'perl.', 'phf.', 'pod.', 'portsweep.', 'rootkit.', 'satan.', 'smurf.', 'spy.', 'teardrop.', 'warezclient.', 'warezmaster.'], 'attack')
dataSet.to_csv('kddcup_Binary.csv')

