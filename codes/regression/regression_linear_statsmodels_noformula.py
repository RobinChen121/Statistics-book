# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:19:22 2019

@author: zhen chen

MIT Licence.

Python version: 3.7


Description: use statsmodels for linear regression without formula
    
"""

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

datas = pd.read_excel(r'D:\Users\chen_\git\Statistics-book\datas\linear_regression.xlsx') # 读取 excel 数据，引号里面是 excel 文件的位置
y = datas.iloc[:, 1] # 因变量为第 2 列数据
x = datas.iloc[:, 2] # 自变量为第 3 列数据
model = sm.OLS(y, x).fit() # 构建最小二乘模型并拟合，
                               #此时不用单独输入 x，y了，而是将自变量与因变量用统计语言公式表示，将全部数据导入
print(model.summary()) # 输出回归结果


# 画图
# 这两行代码在画图时添加中文必须用
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

predicts = model.predict() # 模型的预测值
y = datas.iloc[:, 1] # 因变量为第 2 列数据
x = datas.iloc[:, 2] # 自变量为第 3 列数据
plt.scatter(x, y, label='实际值')
plt.plot(x, predicts, color = 'red', label='预测值')
plt.legend() # 显示图例，即每条线对应 label 中的内容
plt.show() # 显示图形