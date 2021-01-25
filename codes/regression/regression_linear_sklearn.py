# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:18:06 2019

@author: zhen chen

MIT Licence.

Python version: 3.7


Description: linear regression by sklearn
    
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

datas = pd.read_excel(r'D:\Users\chen_\git\Statistics-book\datas\linear_regression.xlsx') # 读取 excel 数据，引号里面是 excel 文件的位置
y = datas.iloc[:, 1] # 因变量为第 2 列数据
x = datas.iloc[:, 2:6] # 自变量为第 3 列到第 6 列数据

# 将 y 分别增加一个轴，以满足 sklearn 中回归模型认可的数据
# 此时由于 x 是多元变量，则不用添加新的轴了
y = y[:, np.newaxis]

model = LinearRegression() # 构建线性模型
model.fit(x, y) # 自变量在前，因变量在后
predicts = model.predict(x) # 预测值
R2 = model.score(x, y) # 拟合程度 R2
print('R2 = %.3f' % R2) # 输出 R2
coef = model.coef_ # 斜率
intercept = model.intercept_ # 截距
print(model.coef_, model.intercept_) # 输出斜率和截距