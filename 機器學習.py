import matplotlib
import numpy as np
import matplotlib.pyplot as plt

x=np.array([[1,5],[3,-4],[7,3],[1,1],[3,3],[6,5],[5,6],[6,4]])
y=np.array([1,1,2,2,3,3,4,5])
#plt.scatter(x[:,0],x[:,1],c=y,s=100)

#SVM
plt.figure()
from sklearn.svm import SVC
clf=SVC()
clf.fit(x,y)
xx=[1,2,3,4]
yy=[5,6,7,8]
X,Y=np.meshgrid(np.linspace(1,7,10),np.linspace(-4,5,10))
X=X.ravel()
Y=Y.ravel()
Z=clf.predict(list(zip(X,Y)))  #需使用array輸入，因此用"zip"
plt.scatter(X,Y,c=Z,s=30)
plt.show()

#Kmeans
plt.figure()
from sklearn.cluster import KMeans
clf=KMeans(n_clusters=4)
x=np.random.rand(100,2)
clf.fit(x)
plt.scatter(x[:,0],x[:,1],c=clf.labels_,s=30,cmap=plt.cm.coolwarm)
plt.show()
