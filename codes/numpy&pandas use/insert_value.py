""" 
3 # @File  : insert_value.py
4 # @Author: Chen Zhen
5 # @Date  : 2019/10/27
6 # @Desc  : insert value to pandasin specific row position

"""

import numpy as np
import pandas as pd

df = pd.DataFrame(np.array([[85, 68, 90], [82, 63, 88], [84, 90, 78]]), columns=['统计学', '高数', '英语'], index=['张三', '李四', '王五'])
print(df)

df1 = pd.DataFrame(np.array([[87, 64, 71]]), columns=['统计学', '高数', '英语'], index=['陈七'])
df = pd.concat([df.iloc[: 1], df1, df.iloc[1:]])
print(df)