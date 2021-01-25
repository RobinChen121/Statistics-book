# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:12:45 2019

@author: zhen chen

MIT Licence.

Python version: 3.7


Description: multi variable linear regression by statsmodels
    
"""

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

datas = pd.read_excel(r'D:\Users\chen_\git\Statistics-book\datas\linear_regression.xlsx') # 读取 excel 数据，引号里面是 excel 文件的位置
y = datas.iloc[:, 1] # 因变量为第 2 列数据
x = datas.iloc[:, 2:6] # 自变量为第 3 列到第 6 列数据
x = sm.add_constant(x) # 若模型中有截距，必须有这一步
model = sm.OLS(y, x).fit() # 构建最小二乘模型并拟合
print(model.summary()) # 输出回归结果



