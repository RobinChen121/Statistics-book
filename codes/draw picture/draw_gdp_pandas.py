# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:28:25 2020

@author: zhen chen

MIT Licence.

Python version: 3.7


Description: 
    
"""

import pandas as pd
import matplotlib.pyplot as plt

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 输入纵坐标轴数据与横坐标轴数据，也可利用 pandas 从 excel 文件中读取数据
gdp_rate = [9.40, 10.60, 9.60, 7.90, 7.80, 7.30, 6.90, 6.70, 6.80, 6.60]
first_industry_rate = [4.00, 4.30, 4.20, 4.50, 3.80, 4.10, 3.90, 3.30, 4.00, 3.50]
second_industry_rate = [10.30, 12.70, 10.70, 8.40, 8.00, 7.40, 6.20, 6.30, 5.90, 5.80]
third_industry_rate = [9.60, 9.70, 9.50, 8.00, 8.30, 7.80, 8.20, 7.70, 7.90, 7.60]
years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

# 将上列数据读取到 pandas 中的 DateFrame 数据表中
df = pd.DataFrame({'年份': years, 'GDP增长率' : gdp_rate, '第一产业增长率' : first_industry_rate, '第二产业增长率' : second_industry_rate, '第三产业增长率' : third_industry_rate})
df.plot(x = '年份', y = ['GDP增长率', '第一产业增长率', '第二产业增长率', '第三产业增长率'], style = ['.-', '.-', '.-', '.-'])