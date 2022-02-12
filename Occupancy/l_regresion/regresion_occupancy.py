import csv
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np


dataset = pd.read_csv('/home/nuria/Documents/Occupancy/Occupancy.csv', header= 0)
headers = list(dataset.columns.values)
#print(headers)
#print(dataset)

x= dataset.drop(['Occupancy', 'date'], axis= 1).values#quitar occupancy y date
y= dataset['Occupancy'].values#la salida
#--Lo mismo:
#x = dataset.iloc[:,1:-1].values
#y = dataset.iloc[:,-1].values

#-- 70% train 30% test y estratificado--
x_train, x_test, y_train, y_test = train_test_split(x,y, train_size= 0.7, stratify=y)

# -- Comprobar las proporciones de 0 y 1----
"""#print(y_train)

num_0= 0
num_1= 0

j= 0

for i in y_train:
	if y_train[j]== 0:
		num_0= num_0+1
	elif y_train[j]== 1:
		num_1= num_1+1
	j= j+1
print("NUMERO DE 0: ",num_0," NUMERO DE 1: ",num_1)"""

# --Regresion Linear--

print("Regresion lineal")

l_regr= LogisticRegression()
# Entrenamiento
l_regr.fit(x_train, y_train)
# Prediccion
occup_pred = l_regr.predict(x_test)

#print("PREDICTION ", pred)

# --- Comprobacion manual del porcentaje de correctas----

correct= 0
wrong= 0

#print("LENGTH y_test: ", len(y_test))

"""for i in range(len(y_test)):
	#occup_pred no tiene valores exactos de 0 y 1 luego:
	y= occup_pred[i]
	if(y >= 0.5):
		y= 1
	else:
		y= 0
	#---------
	#print("PRED[I]: ",occup_pred[i],"---> Y: ",y," Y_TEST[I]: ",y_test[i])
	if y == y_test[i]:
		correct= correct+1
	else:
		wrong= wrong+1

print("Correct: ",correct, " Wrong: ",wrong, "TOTAL: ",len(y_test))
print("TOTAL CORRECT :",correct/(len(y_test)))
#print("Mean squared error: %2.f"% mean_squared_error(y_test, pred))"""
#-------------------------------------

accuracy = metrics.accuracy_score(y_test, occup_pred)*100
print("Accuracy: ","{:.1f}".format(accuracy),"%")
#Lo mismo: 
#accuracy = l_regr.score(x_test,y_test)*100
#print("Accuracy: ","{:.1f}".format(accuracy),"%")
precision = metrics.precision_score(y_test, occup_pred)*100
print("Precision: ","{:.1f}".format(precision),"%")
recall = metrics.recall_score(y_test, occup_pred)*100
print("Recall: ","{:.1f}".format(recall),"%")

