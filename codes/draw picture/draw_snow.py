# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 22:32:58 2020

@author: zhen chen

MIT Licence.

Python version: 3.7


Description: 
    
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def draw_scenery():
    """绘制雪景图"""
    
    im = Image.open('brage.png')
    bg = np.array(im)
    plt.imshow(bg) # 绘制背景图
    
    for i in range(80):
        x = np.random.randint(80, im.size[0]-80)
        y = np.random.randint(30, im.size[1]-30)
        r = np.random.randint(5, 20)
        a = np.random.random()*0.6 + 0.2
        v = np.array((x-r/2, y))
        u = np.array((x+r/2, y))
        w = rotate(v-u, 60) + u
        
        data = np.array(snow([(u[0],u[1]),(w[0],w[1]),(v[0],v[1])], 5))
        x, y = np.split(data, 2, axis=1)
        plt.plot(x, y, c='#AABBCC', lw=1, ls='-', alpha=a)
    
    plt.axis('equal') 
    plt.show()

draw_scenery()
