import pandas as pd
data = pd.read_csv('irrigation.csv') 
data.fillna("0", inplace=True)
sen1=data['sensor1']
sen2=data['sensor2']
outcome=data['Outcome']
#print(data.isnull().sum())

#y=mx+c

#x=sensor1

#print(sen1)

#LINEARREGRESSION:m=x-x_(y-y_)/(x-x_)

#x_(X bar)
total=0
for x in range(0,len(sen1)):
    total=total+int(sen1[x])
    xbar=total/len(sen1)
# print(xbar)

#X-xbar
# print(len(sen1))

x_xbar=[]
for d in range(0,len(sen1)):
    x_xbar.append(int(sen1[d]) - xbar)
    # print(x_xbar)

#y(Y bar)
ybar=0
for i in range(0,len(outcome)):
    ybar=ybar+int(outcome[i])
    y_bar=ybar/len(outcome)
# print(y_bar)

#y-ybar
y_ybar=[]
for r in range(1,len(outcome)):
    y_ybar.append(int(outcome[r])-ybar)
# print(y_ybar[r])


#x-xbarwholesqaure
t=x_xbar[d]*x_xbar[d]
# print(t)

#x-xbar * y-ybar
wax=[]
for f in range(0,len(sen1)-1):
    wax.append(x_xbar[f] * y_ybar[f]) 
    # print(wax[f])

#m
h=t/wax[f]
print(h)

#c
c=h*xbar-y_bar
print(c)

y = h * 700 + c
print(y)
