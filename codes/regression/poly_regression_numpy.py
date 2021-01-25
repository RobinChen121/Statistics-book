# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:38:21 2019

@author: zhen chen

MIT Licence.

Python version: 3.7


Description: polynomial regreession by numpy
    
"""

import numpy as np
import matplotlib.pyplot as plt


sales_datas = [0.5, 9.36, 52, 191, 350, 571, 912, 1207, 1682.69, 2135]
year = np.arange(2009, 2019)
year_num = np.arange(1, 11) # 用年的序号作为自变量，预测效果更好些

# 画图
# 这两行代码使得 pyplot 画出的图形中可以显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.plot(year, sales_datas, 'o-', label = '公布销售额') # 折线图


# 拟合
fit_parameters = np.polyfit(year_num, sales_datas, deg=3) # 拟合成三次方
print(fit_parameters) # 输出拟合的参数值, 最高次项的系数值在最前面
forecast_function = np.poly1d(fit_parameters)  # 预测（拟合）的函数

# 预测
forecast2019 = forecast_function(11) # 2019 是第11年
print(forecast2019) # 输出 2019 年的预测结果

forecasts = forecast_function(np.arange(1, 12))
plt.plot(np.append(year, 2019), forecasts, 'o:', label='预测销量')
plt.legend() # 显示图例, 图例中内容由 label 定义
plt.show()





