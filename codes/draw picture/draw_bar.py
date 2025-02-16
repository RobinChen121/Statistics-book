#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

# @Time    : 2019/8/23 15:13
# @Author  : Zhen Chen

# Python version: 3.7
# Description: 画条形图

"""
# import matplotlib.pyplot as plt
# import numpy as np
#
# # 这两行代码解决 plt 中文显示的问题
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
#
# # 输入统计数据
# waters = ('碳酸饮料', '绿茶', '矿泉水', '果汁', '其他')
# buy_number_male = [6, 7, 6, 1, 2]
# buy_number_female = [9, 4, 4, 5, 6]
#
# bar_width = 0.3  # 条形宽度
# index_male = np.arange(len(waters))  # 男生条形图的横坐标
# index_female = index_male + bar_width  # 女生条形图的横坐标
#
# # 使用两次 bar 函数画出两组条形图
# plt.bar(index_male, height=buy_number_male, width=bar_width, color='b', label='男性')
# plt.bar(index_female, height=buy_number_female, width=bar_width, color='g', label='女性')
#
# plt.legend()  # 显示图例
# plt.xticks(index_male + bar_width/2, waters)  # 让横坐标轴刻度显示为 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
# plt.ylabel('购买量')  # 纵坐标轴标题
# plt.title('购买饮用水情况的调查结果')  # 图形标题
#
# plt.show()

 import matplotlib.pyplot as plt

 # 这两行代码解决 plt 中文显示的问题
 plt.rcParams['font.sans-serif'] = ['SimHei']
 plt.rcParams['axes.unicode_minus'] = False

 waters = ('碳酸饮料', '绿茶', '矿泉水', '果汁', '其他')
 buy_number = [6, 7, 6, 1, 2]

 plt.barh(waters, buy_number)  # 横放条形图函数 barh
 plt.title('男性购买饮用水情况的调查结果')

 plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

waters = ('碳酸饮料', '绿茶', '矿泉水', '果汁', '其他')
buy_number_male = [6, 7, 6, 1, 2]
buy_number_female = [9, 4, 4, 5, 6]

df = pd.DataFrame({'男性': buy_number_male, '女性': buy_number_female}, index=waters)

df.plot(kind='bar', rot=0)
plt.show()

sns.set()
sns.barplot(waters, buy_number_male)


