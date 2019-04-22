import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import style
style.use('ggplot')

dataset = pd.read_csv('C:\\Users\\omkar waghmare\\Desktop\\practicals\\LP3\\dataset_linear_regression.csv')
#dataset = pd.read_csv('C:\\Users\\omkar waghmare\\Desktop\\practicals\\LP3\\Book1.csv')
X = dataset.iloc[:,0].values
y = dataset.iloc[:,1].values

#calculation

#finding b1
def find_b1(X,y):
    mean_X = np.mean(X) # mean of x
    mean_y = np.mean(y) #mean of y
    sum_diff_X = 0
    sum_diff_X_y = 0
    for i,j in zip(X,y):
        diff_X = i - mean_X #(xi - x_mean)
        sum_diff_X = sum_diff_X + np.square(diff_X) #sum of ((xi - x_mean)^2)
        diff_y = j - mean_y #(yi - y_mean)
        sum_diff_X_y = sum_diff_X_y + (diff_X * diff_y) #sum of ((xi - x_mean)*(yi - y_mean))
    
    b1 = sum_diff_X_y/sum_diff_X
    return b1,mean_X,mean_y

#finding b0
def find_b0(b1,mean_X,mean_y):
    b0 = mean_y - (b1*mean_X)
    return b0

#finding Sum of Square errors
def find_SSE(X,y,b0,b1):
    SSError = 0
    i = 0
    for j,k in zip(X,y):
        val = ((b0 + b1*j) - k) # outputs predicted value - actual value -> error
        SSError = SSError + np.square(val) # sums and squares the error
        i = i+1
    return SSError


#finding coefficient of determination Rsq
def find_rsq(SSError,mean_y): #in order to find rsq we need to find out SST(initial with only y) and SSE(with x and y) 
    SSTotal = 0
    for i in y:
        SSTotal = SSTotal +np.square(i-mean_y) #SST find with only sum((y-y_mean)^2) here y_mean is considered as the predicted value
        SSReg = SSTotal - SSError
    return (SSReg / SSTotal)*100

#predicting value
def pred(b0,b1,user_input):
    pred_val = (b0 + int(user_input)*b1) #convert accepted value into int
    return pred_val

#plotting a scatter plot
def plot(x,y,b0,b1):
    var = []
    for i,j in enumerate(x):
        var.insert(i,pred(b0,b1,j)) 
        print(var[i])
    plt.scatter(X,y,marker="o",label = 'actual points')
    plt.plot(X,var,'g',label = 'best fit',linewidth= 5)
    plt.xlabel('indepedent')
    plt.ylabel('dependent')
    plt.title('best fit line')
    plt.legend()
    plt.show()
    return 0

b1,mean_X,mean_y = find_b1(X,y)
b0 = find_b0(b1,mean_X,mean_y)
SSError = find_SSE(X,y,b0,b1)
rsq = find_rsq(SSError,mean_y)
user_input = input("enter the value of X for which y is to be predicted: ")
pred_val = pred(b0,b1,user_input)
print("Y = ",b0,"+",b1,"x")
print(SSError)
print(rsq)
print("predicted value is :",pred_val)
plot(X,y,b0,b1)
