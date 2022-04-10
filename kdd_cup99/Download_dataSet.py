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
s= 1976080 # Leer solo el 40%
skip= sorted(random.sample(range(n),n-s))
dataset = pd.read_csv('/home/nuriadj/Documents/TFG/kdd_cup99/kddcup.data', skiprows=skip)
print("Leido un: ",(len(dataset)*100)/n,"% del csv")
headers = list(dataset.columns.values)

#dataset= pd.read_csv('/home/nuriadj/Documents/TFG/kdd_cup99/kddcup.data')

#change Multi-class to binary-class
dataset['normal.'] = dataset['normal.'].replace(['back.', 'buffer_overflow.', 'ftp_write.', 'guess_passwd.', 'imap.', 'ipsweep.', 'land.', 'loadmodule.', 'multihop.', 'neptune.', 'nmap.', 'perl.', 'phf.', 'pod.', 'portsweep.', 'rootkit.', 'satan.', 'smurf.', 'spy.', 'teardrop.', 'warezclient.', 'warezmaster.'], 'attack')

#headers = list(dataset.columns.values)


#Eliminar datos Redundantes
dataset.drop(dataset.columns[19], axis= 1, inplace= True)
dataset.drop(dataset.columns[20], axis= 1, inplace= True)


# In[257]:

#print(dataset.dtypes)
#print("Primera FILA: ",dataset.iloc[0])

#Las tres primeras columnas contienen strings

dataset['tcp'] = dataset['tcp'].astype('category')
dataset['http'] = dataset['http'].astype('category')
dataset['SF'] = dataset['SF'].astype('category')
cat_columns = dataset.select_dtypes(['category']).columns
dataset[cat_columns] = dataset[cat_columns].apply(lambda x: x.cat.codes)
#print("\\nafter:\\n",pd.DataFrame(dataset, columns=[0]).dtypes)')


# In[258]:

#print("Numero de duplicados: ",dataset[dataset.duplicated(keep=False)])
#Eliminar duplicados
dataset.drop_duplicates(subset=None, keep='first', inplace=True)

#Eliminar cabecera e indice
dataset.to_csv('kddcup_40_perClean.csv', header= False, index= False)

