
from sklearn.metrics import mean_absolute_error as mae

xdata = [1,2,1,2,3,4,2,5]
ydata = [2,1,1,2,3,4,3,5]

print('MAE')
print(mae(xdata,ydata))
"""
MAE
0.375
"""
