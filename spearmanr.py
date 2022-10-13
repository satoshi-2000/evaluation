# This code is based on this article.
# https://qiita.com/dacciinfo/items/88debe69f9f4e927aafc

from scipy.stats import spearmanr

xdata = [1,2,1,2,3,4,2,5]
ydata = [2,1,1,2,3,4,3,5]

correlation, pvalue = spearmanr(xdata, ydata)
print(correlation) #0.6727272727272726
"""
0.83756543735604
0.009451676093682563
"""
