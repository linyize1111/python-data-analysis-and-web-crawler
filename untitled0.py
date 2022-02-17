
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import pandas as pd
fig=plt.figure(figsize=(10,10))
ax1=fig.add_subplot(111,projection='3d')

x=[]
y=[]
z=[]
w=[]
x=np.linspace(0,10,1000)
y=np.cos(x)
z=np.random.randint(0,10,1000)
plt.plot(x,y)
plt.plot(x,z)
ax1.scatter3D(x,y,z)
plt.show()
w=x
#w=x<0  #篩出array中<0者
#print(w)
#print(w[w<2])
#plt.plot(x[w<2],w[w<2])
#%matplotlib qt #互動式視窗
#取 dataframe單項資料的方法
#dataframe名稱[項目名稱]
#或是
#dataframe名稱.項目名稱
#轉換dataframe單項資料成array的方法
#dataframe名稱[項目名稱].values
#或是
#dataframe名稱.項目名稱.values
#畫單項資料直方圖的方法
#dataframe名稱.項目名稱.hist ( bins = 區分區間)
#e.g. df=pd.read_csv("grades.csv")→df.head( )
#平均/標準差：df.項目名稱.mean( )/df.項目名稱.std( )
#統計數據大補帖：df.describe( )，跑出平均、標準差……等
#所有項目的相關係數：df.corr( )
#兩兩項目的相關係數：df.項目名稱1.corr(df.項目名稱2)
#新增總和欄位：df["新增欄位名稱"]=df[[要總和欄位的list]].sum(1是每行項目加總/0是每列項目加總)
#e.g. df["主科"]=df.數學*1.5+df.英文
#排序(由大到小)：df.sort_values(by="要排序項目",ascending=Fasle)
#排序(由小到大)：df.sort_values(by="要排序項目")
#e.g. df.sort_values(by=["主科", "總級分"], ascending=False)
mydata1=np.random.randn(3,4)
df1=pd.DataFrame(mydata1,columns=list("abcd"))
print(df1)
df2=pd.DataFrame(np.random.randn(5,4),columns=list("abcd"))
df3=pd.concat([df1,df2],axis=0) #先烈後行
df3.index=range(8)
print(df3)
 


mydata2=pd.read_csv("http://bit.ly/uforeports")
df4=pd.DataFrame(mydata2)
print(df4)
df_state=df4.groupby("State").count()
print(df_state)
df5=df_state.sort_values(by="Time",ascending=False)
print(df5)
df5.plot()
df_state.Time.plot(kind="bar")
#DataFrame名稱.loc[條件,col_indexer] = value instead
print(df2.loc[2:5, "a":"d"])


