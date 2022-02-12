import csv
import pandas as pd
import numpy as np
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from collections import Counter

dataset = pd.read_csv('/home/nuria/Documents/Occupancy/Occupancy.csv', header= 0)
headers = list(dataset.columns.values)


x= dataset.drop(['Occupancy', 'date'], axis= 1).values#quitar occupancy y date
y= dataset['Occupancy'].values#la salida

#print(Counter(y))

#-- 70% train 30% test y estratificado--
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.3, stratify=y)


#Comprobar que el stratify lo esta haciendo bien:
#print(Counter(y_train))
#print(Counter(y_test))
#----------------------

print("Maquina de soporte vectorial")

svm= svm.SVC()
svm.fit(x_train, y_train)

occup_pred = svm.predict(x_test)

accuracy= metrics.accuracy_score(y_test, occup_pred)*100

#print("Numero de vectores soporte: ", svm.n_support_)
accuracy = metrics.accuracy_score(y_test, occup_pred)*100
print("Accuracy: ","{:.1f}".format(accuracy),"%")
precision = metrics.precision_score(y_test, occup_pred)*100
print("Precision: ","{:.1f}".format(precision),"%")
recall = metrics.recall_score(y_test, occup_pred)*100
print("Recall: ","{:.1f}".format(recall),"%")
