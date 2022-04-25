# 相関行列
import numpy as np

xdata = [1,2,1,2,3,4,2,5]
ydata = [2,1,1,2,3,4,3,5]

print(np.corrcoef(xdata,ydata))
"""
[[1.      0.89687]
 [0.89687 1.     ]]
 """
