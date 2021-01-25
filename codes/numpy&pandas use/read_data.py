# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:09:21 2020

@author: zhen chen

MIT Licence.

Python version: 3.7


Description: read data from local pc
    
"""
import pandas as pd

df = pd.read_excel(r'D:\Users\chen_\git\Statistics-book\datas\sta-data-cluster.xlsx', index_col=0)

print(df)