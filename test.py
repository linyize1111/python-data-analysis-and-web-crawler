import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,]
y1 = [1,2,3,4,55,6,6,7]

y2 = [6,20,9,2,5,8,2,8,]

plt.plot(x,y1)
plt.plot(x,y2)

plt.legend(['y1','y2'])
plt.show()