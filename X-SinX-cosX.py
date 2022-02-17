import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fig=plt.figure(figsize=(10,10))
ax1=fig.add_subplot(111,projection='3d')

x=[]
y=[]
z=[]
x=np.linspace(-8,80,500)
y=np.sin(x)
z=np.cos(x)

ax1.scatter3D(x,y,z,color='green')

ax1.set_xlabel("X")
ax1.set_ylabel("Y - SinX")
ax1.set_zlabel("Z - CosX")
my_cmap = plt.get_cmap('hsv')
sctt = ax1.scatter3D(x, y, z,
                    alpha = 0.9, #透明度
                    c = (x + y + z), #數據大小於漸層表值
                    cmap = my_cmap, #採用"hsv"作為色系map
                    marker ='*')#標記
fig.colorbar(sctt, ax = ax1, shrink = 10, aspect = 0.8)
plt.show()