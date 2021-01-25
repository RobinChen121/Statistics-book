# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 19:31:42 2020

@author: zhen chen

MIT Licence.

Python version: 3.7


Description: use k-means for cluster analysis
    
"""


import pandas as pd
from sklearn.cluster import KMeans
from sklearn import datasets
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


df = pd.read_excel(r'D:\Users\chen_\git\Statistics-book\datas\sta-data-cluster.xlsx', index_col=0)

kmeans = KMeans(n_clusters=3).fit(df.values) # 分为 3 类
print(kmeans.labels_) # 输出判别结果列表

# 具体输出判别结果
cluster_1 = []
cluster_2 = []
cluster_3 = []
for i, j in enumerate(kmeans.labels_):
    if j == 0:
        cluster_1.append(df.index[i])
    elif j == 1:
        cluster_2.append(df.index[i])
    else:
        cluster_3.append(df.index[i])
print('类别1')
print(cluster_1)
print('类别2')
print(cluster_2)        
print('类别3')
print(cluster_3)        

iris = datasets.load_iris() # 调用数据
X = iris.data
y = iris.target # y 为实际分类结果

kmeans = KMeans(n_clusters=3).fit(X) # 聚类

# 画图
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter3D(X[:, 3], X[:, 0], X[:, 2], c = kmeans.labels_) # 取了原始数据三列，画出 3d 散点图
plt.show()



