import pandas as pd
import numpy as np
import math

def distance(pointA , pointB) :
    x_dist = (pointB[0] - pointA[0])**2
    y_dist = (pointB[1] - pointA[1])**2
    return(math.sqrt(x_dist+y_dist))



dataset = pd.read_csv('C:/Users/omkar waghmare/Desktop/practicals/LP3/KNN_dataset.csv')
train_set = dataset.iloc[: , 0:2]
test_set = dataset.iloc[6 , 0:2]
shape = dataset.iloc[: , 2]

print('To find the class of point (6,6)')
print('\n\nDataset :')
print(dataset)
K = int(input('enter the value of K : '))

eucledian_distance = pd.DataFrame(columns=['dist']) 
neighbors = pd.DataFrame(columns=['k_closest'])
#calculating distance of the new point from every point in the training set
j = 0
i = 0
while i< len(dataset.index)-1 :
    pointA = train_set.iloc[i , :]
    i = i+1
    pointB = test_set
    dist = distance(pointB,pointA)
    eucledian_distance.loc[j] = dist
    j = j + 1

#sorting the distances in ascending order
eucledian_distance = eucledian_distance.sort_values(by='dist')

#selecting the closest 'k' neighbours
neighbors = eucledian_distance.head(K)

#finding their class and storing it in response df
#index = neighbors.index

class_votes = {}
for x in neighbors.index:
    value = shape.loc[x]
    if value in class_votes:
        class_votes[value] += 1
    else:
        class_votes[value] = 1

print(max(class_votes))  

