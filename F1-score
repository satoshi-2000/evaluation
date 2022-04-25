# This code is besed on this article.
# https://qiita.com/keiji_dl/items/0a8130aea8233fca92e0#Chapter12

# 混合行列の作成
tp = 0
tn = 0
fp = 0
fn = 0

xdata = [1,2,1,2,3,4,2,5]
ydata = [2,1,1,2,3,4,3,5]

for pred, ans in zip(xdata, ydata):
    if pred == ans:
        if pred ==1:
            tp += 1
        else:
            tn += 1
    elif pred == 0:
        fn += 1
    elif pred == 1:
        fp +=1

recall = tp/(tp+fn)
print("Recall")
print(recall)

precision = tp/(tp+fp)
print("Precission")
print(precission)

f1score = 2 * precision * recall / (precision + recall)
print("F1score")
print(f1score)

print(tp,tn,fp,fn)
"""
Recall
1.0
Precission
0.625
F1score
0.6666666666666666
1 4 1 0
"""
