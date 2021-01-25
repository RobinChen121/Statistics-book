#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

# @Time    : 2019/8/23 20:11
# @Author  : Zhen Chen

# Python version: 3.7
# Description: 画直方图

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns


x = [141, 159, 166, 172, 177, 182, 188, 196, 203, 214,
     143, 160, 167, 173, 177, 183, 189, 196, 203, 215,
     144, 160, 168, 173, 178, 184, 189, 196, 205, 218,
     149, 161, 168, 174, 178, 185, 189, 196, 206, 223,
     150, 161, 168, 174, 178, 186, 190, 196, 207, 225,
     152, 162, 170, 174, 179, 186, 190, 197, 208, 226,
     153, 163, 171, 175, 179, 187, 191, 197, 209, 228,
     153, 163, 171, 175, 179, 187, 192, 198, 210, 233,
     154, 164, 172, 175, 180, 187, 194, 198, 210, 233,
     155, 165, 172, 175, 180, 187, 194, 200, 211, 234,
     156, 165, 172, 176, 181, 188, 195, 201, 211, 234,
     158, 165, 172, 176, 182, 188, 195, 202, 213, 237]

#x = [140,130,120,110,100,100,90,90,90,70,60,60,60,60,60,40,40,40,40]
x = [410,330,320,300,210,170,170,150,150]

# the histogram of the data
n, bins, patches = plt.hist(x, 5, edgecolor='k', alpha=0.35) # 设置直方边线颜色为黑色，不透明度为 0.35
sns.set()

#hist, bins = np.histogram(x, bins=6)
#bin_centers = (bins[1:]+bins[:-1])*0.5
#plt.plot(bin_centers, hist)
plt.show()

mean = np.mean(x)
print('mean is %.2f' % mean)
variance = np.var(x)
std = np.sqrt(variance)
print(' std is %.2f' % std)
skew = stats.skew(x)
print('skew is %.2f' % skew)
kurt = stats.kurtosis(x)
print('kurt is %.2f' % kurt)
