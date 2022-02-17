import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
x=np.linspace(0,5,50)
y=x*1.2+0.8
line1=plt.plot(x,y,'r',label="ClassicLine")
plt.scatter(x,x*1.2+0.8+np.random.randn(50))
regr = LinearRegression()
y=x*1.2+0.8+np.random.randn(50)*0.6
X=x.reshape(50,1)
regr.fit(X,y)
Y=regr.predict(X)
line2=plt.plot(x,Y,'g',label="LinearRegr")
plt.legend(loc='upper right', shadow=True) 
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=50,test_size=20)
x_train.shape=(30,1)
x_test.shape=(20,1)
plt.figure()
regr.fit(x_train,y_train)
plt.scatter(x_train,y_train)
plt.plot(x_train,regr.predict(x_train),'r',label="train")
plt.figure()
plt.scatter(x_test,y_test)
plt.plot(x_test,regr.predict(x_test),'g',label="test")
plt.show()