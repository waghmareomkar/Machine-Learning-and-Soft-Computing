import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd

#accessing data
dataset = pd.read_csv("/home/omkar/Downloads/cosmetics.csv") #data ACCEPT
print(dataset.head())
#
# #splitting data
X = dataset.drop(['ID'] , axis= 1) # axis =1 , coloumn,
X = X.iloc[:,:-1].values #indexing and splitting data
y = dataset.iloc[:,-1].values

print(X)
#
# #label encoding the data
age_encode = LabelEncoder()
income_encode = LabelEncoder()
gender_encode = LabelEncoder()
MS_encode = LabelEncoder()
buys_encode = LabelEncoder()

X[:,0] = age_encode.fit_transform(X[:,0])
X[:,1] = income_encode.fit_transform(X[:,1])
X[:,2] = gender_encode.fit_transform(X[:,2])
X[:,3] = MS_encode.fit_transform(X[:,3])
y = buys_encode.fit_transform(y)


print(X)

#
# #splitting the data into training and testing sets
#
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.20, random_state=42)

print(X, "          ", y)
# implementing decision tree using sklearn
from sklearn import tree
model = tree.DecisionTreeClassifier() # create an object
model.fit(X_train,y_train) #fit it
print(model.predict([[1,1,1,1]])) # accepts a 2D array only !!, predict values
#
#visualizing decision tree
from subprocess import call
import graphviz
tree.export_graphviz(model, out_file='tree.dot', feature_names=["AGE","INCOME","GENDER","MARITIAL STATUS"], class_names=["YES","NO"],filled=True,rounded=True)
call(['dot', '-Tpng', 'tree.dot', '-o', 'tree2.png', '-Gdpi=600'])
