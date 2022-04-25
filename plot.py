# This code is based on this article.
# https://www.delftstack.com/ja/howto/matplotlib/set-color-for-scatterplot-in-matplotlib/

import matplotlib.pyplot as plt

xdata = [1,2,1,2,3,4,2,5]
ydata = [2,1,1,2,3,4,3,5]
zdata = [2,4,1,1,3,4,2,4]

# 散布図を作成 (cで色を設定)
plt.scatter(xdata,ydata,c="red")
plt.scatter(xdata,zdata,c="blue")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
