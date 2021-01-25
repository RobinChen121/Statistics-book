# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:21:01 2019

@author: zhen chen

MIT Licence.

Python version: 3.7


Description: polynomial regression by sklearn
    
"""

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score #导入计算均方误差，拟合优度的函数
from sklearn.preprocessing import PolynomialFeatures # 导入处理多项式拟合的函数
import numpy as np
import matplotlib.pyplot as plt

sales_datas = [0.5, 9.36, 52, 191, 350, 571, 912, 1207, 1682.69, 2135]
year = np.arange(2009, 2019)
year_num = np.arange(1, 11) # 用年的序号作为自变量，预测效果更好些

# sklearn 的自变量和因变量
x = year_num[:, np.newaxis]
sales_datas = np.array(sales_datas)
y = sales_datas[:, np.newaxis]

polynomial_features= PolynomialFeatures(degree=3) # 多项式最高次方数为3
x_poly = polynomial_features.fit_transform(x) # 对自变量处理

#在上面把自变量用多项式处理函数处理后，再用线性拟合得出拟合的参数值和预测值
model = LinearRegression()
model.fit(x_poly, y)
predicts = model.predict(x_poly) # 原始数据的预测值

forecast_year = np.array([11])  # 2019 是第 11 年  
forecast_year = forecast_year[np.newaxis]
forecast_year_poly = polynomial_features.fit_transform(forecast_year) # 对自变量处理
print(model.coef_, model.intercept_) # 输出斜率（斜率里也包括自变量零次方的系数）和截距
forecast2019 = model.predict(forecast_year_poly) # 2019 是第11年
print(forecast2019) # 输出 2019 年的预测结果

rmse = np.sqrt(mean_squared_error(y,predicts)) #拟合均方跟误差
R2 = r2_score(y, predicts) #拟合优度
print(rmse)
print(R2)

# 画图
# 这两行代码使得 pyplot 画出的图形中可以显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.plot(year, sales_datas, 'o-', label = '公布销售额') # 折线图
predict_values = np.append(list(predicts.flat),list(forecast2019.flat)) # flattern the ndarray
plt.plot(np.append(year, 2019), predict_values, 'o:', label='预测销量')
plt.legend() # 显示图例, 图例中内容由 label 定义
plt.show()


