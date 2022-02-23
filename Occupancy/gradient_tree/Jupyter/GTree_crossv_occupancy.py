#!/usr/bin/env python
# coding: utf-8

# In[33]:


get_ipython().run_cell_magic('time', '', 'import csv\nimport pandas as pd\nimport numpy as np\nfrom sklearn import metrics\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import GradientBoostingClassifier\nfrom sklearn.model_selection import StratifiedKFold, KFold')


# In[34]:


get_ipython().run_cell_magic('time', '', "dataset = pd.read_csv('/home/nuria/Documents/Occupancy/Occupancy.csv', header= 0)\nheaders = list(dataset.columns.values)")


# In[35]:


get_ipython().run_cell_magic('time', '', "x= dataset.drop(['Occupancy', 'date'], axis= 1).values#quitar occupancy y date\ny= dataset['Occupancy'].values#la salida")


# In[36]:


get_ipython().run_cell_magic('time', '', '#-- 70% train 30% test y estratificado--\nx_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.3, stratify=y)')


# In[37]:


get_ipython().run_cell_magic('time', '', '#skf = StratifiedKFold(n_splits= 5)\nskf = KFold(n_splits= 5)\ngtb = GradientBoostingClassifier()\n\nacc_score= []\nprec_score= []\nrec_score= []')


# In[38]:


get_ipython().run_cell_magic('time', '', 'for train_index, test_index in skf.split(x_train, y_train):\n    x_subtrain, x_subtest = x_train[train_index,:], x_train[test_index,:]\n    y_subtrain, y_subtest = y_train[train_index], y_train[test_index]\n    \n    gtb.fit(x_subtrain, y_subtrain)\n    \n    pred_values = gtb.predict(x_subtest)\n    \n    acc = metrics.accuracy_score(y_subtest, pred_values)*100\n    acc_score.append("{:.1f}".format(acc)+"%")\n    prec = metrics.precision_score(y_subtest, pred_values)*100\n    prec_score.append("{:.1f}".format(prec)+"%")\n    rec = metrics.recall_score(y_subtest, pred_values)*100\n    rec_score.append("{:.1f}".format(rec)+"%")')


# In[39]:


get_ipython().run_cell_magic('time', '', "print('Accuracy of each fold', acc_score)\nprint('Precision of each fold', prec_score)\nprint('Recall of each fold', rec_score)")


# In[40]:


get_ipython().run_cell_magic('time', '', 'occup_pred = gtb.predict(x_test)\n\naccuracy= metrics.accuracy_score(y_test, occup_pred)*100\nprint("Accuracy {:.1f}".format(accuracy),"%")\nprecision = metrics.precision_score(y_test, occup_pred)*100\nprint("Precision: ","{:.1f}".format(precision),"%")\nrecall = metrics.recall_score(y_test, occup_pred)*100\nprint("Recall: ","{:.1f}".format(recall),"%")')
