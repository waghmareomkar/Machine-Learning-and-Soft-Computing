import pandas as pd
import math
from operator import itemgetter

#for knn work with pandas, as we need class aswell which can be character
#for indexing and slicing in pandas use .iloc function
#given k =3
k= 3

#reading the data

dataset = pd.read_csv("/home/omkar/Documents/Untitled1.csv")
print(dataset.head())
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

point_x = int(input("enter x co-ordinate"))
point_y = int(input("enter y co-ordinate"))

#calculating eucledian distance
def distance(point_x,point_y):
    dist = []
    for i in range(len(X)):
        temp = math.sqrt((point_x - X.iloc[i,0])**2+(point_y - X.iloc[i,1])**2)
        dist.append((temp,y[i]))

    return pd.DataFrame(dist) #a data frame acceps list of tuples, but not just a list

def select_class(dist,k):
    dist = dist.sort_values(by=[0]) #important
    temp = dist.head(k)
    #print(temp)
    return (temp.iloc[:,1].mode().iloc[0])

dist = distance(point_x,point_y)
cl = select_class(dist,k)
print(cl)