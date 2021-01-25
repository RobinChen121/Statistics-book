# -*- coding: utf-8 -*-
"""
Created on Mon May  4 20:03:54 2020

@author: zhen chen

MIT Licence.

Python version: 3.7


Description: 
    
"""

import pandas as pd

def replace_score(x):
    if x >= 90:
        return '优'
    elif x >= 80:
        return '良'
    elif x >= 60:
        return '中'
    else:
        return '差'

df1 = pd.DataFrame({'统计学': [85, 68, 90], '高数': [82, 63, 88], '英语': [84, 90, 78]}, index=['张三', '李四', '王五'])
df2 = pd.DataFrame({'统计学': [83, 59], '高数': [92, 70], '英语': [94, 78]}, index=['马六', '陈八'])
df3 = pd.DataFrame({'会计': [75, 78, 80], '管理学': [94, 96, 88]}, index=['张三', '李四', '王五'])
df5 = pd.DataFrame({'姓名': ['张三', '李四', '王五'], '统计学': [85, 68, 90], '高数': [82, 63, 88], '英语': [84, 90, 78]})
df4 = pd.DataFrame({'姓名': ['马六', '陈八'], '统计学': [83, 59], '高数': [92, 70], '英语': [94, 78]})
df6 = pd.DataFrame({'班级': ['一班', '二班', '一班'], '姓名': ['张三', '李四', '王五'], '统计学': [85, 68, 90], '高数': [82, 63, 88], '英语': [84, 90, 78]})
df7 = pd.DataFrame({'班级': ['一班', '二班'], '姓名': ['马六', '陈八'], '统计学': [83, 59], '高数': [92, 70], '英语': [94, 78], '管理学': [94, 96]})
df = pd.DataFrame({'统计学': [85, 68, 90], '高数': [82, 63, 88], '英语': [84, 90, 78], '姓名': ['张三', '李四', '王五']})
print(df.iloc[0].apply(replace_score))