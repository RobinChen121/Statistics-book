#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

# @Time    : 2019/9/15 19:59
# @Author  : Zhen Chen

# Python version: 3.7
# Description: 用 pandas 创建一个 DataFrame 类型

"""

import pandas as pd
import numpy as np

df = pd.DataFrame([['一班', '男', 85, 68, 90], ['二班', '男', 82, 63, 88], ['二班', '女',84, 90, 78], ['三班', '女',75, 68, 80],\
                   ['二班', '女',69, 55, 63], ['一班', '男', 89, 95, 93]], columns=['班级','性别','统计学','高数','英语'],\
                   index=['张三', '李四', '王五', '马六', '陈七', '魏八'])
print(df.groupby(['班级']).mean())

