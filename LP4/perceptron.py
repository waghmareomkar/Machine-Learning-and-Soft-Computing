x1=[]
x2=[]
t=[]
w1=0
w2=0
b=0
y=0
alp=0
b=0
yin=0

def active(y):
    if(y>0):
        return 1
    else:
        return 0



def ino():
    n=int(input("enter no of inputs"))
    print("ENter x1 array:")
    for i in range(n):
        x1.append(int(input()))
    print("ENter x2 array:")
    for i in range(n):
        x2.append(int(input()))
    print("ENter t array:")
    for i in range(n):
        t.append(int(input()))
    w1=int(input("enter w1:"))
    w2=int(input("enter w2:"))
    alp=int(input("enter alp:"))
    b=int(input("enter bias:"))
    for i in range(n):
        yin=(w1*x1[i] + w2*x2[i])+b
        y=active(yin)
        print("Input"+str(i)+" y="+str(y))
        if(y!=t[i]):
            w1=w1+(alp*t[i]*x1[i])
            w2=w2+(alp*t[i]*x2[i])
            b=b+alp*t[i]
            print("new w1=" + str(w1) + " new w2=" + str(w2)+" new b="+str(b))


ino()



