# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 20:49:37 2019

@author: zhen chen

MIT Licence.

Python version: 3.7


Description: use scipy for regression
    
"""

import scipy.stats as st
import pandas as pd

datas = pd.read_excel(r'D:\Users\chen_\git\Statistics-book\datas\linear_regression.xlsx') # 读取 excel 数据，引号里面是 excel 文件的位置
y = datas.iloc[:, 1] # 因变量为第 2 列数据
x = datas.iloc[:, 2] # 自变量为第 3 列数据

# 线性拟合，可以返回斜率，截距，r 值，p 值，标准误差
slope, intercept, r_value, p_value, std_err = st.linregress(x, y) 

print(slope)# 输出斜率
print(intercept) # 输出截距
print(r_value**2) # 输出 r^2
