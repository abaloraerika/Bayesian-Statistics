# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:20:34 2024

@author: abaloraerika
"""

import matplotlib.pyplot as plt
import numpy as np


x = np.random.rand(50) * 10 
y = x * 2 + np.random.randn(50) * 2  


plt.scatter(x, y)


m, b = np.polyfit(x, y, 1)


plt.plot(x, m*x + b, color='blue')


plt.title('Scatter Plot with Regression Line')
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')


plt.show()

