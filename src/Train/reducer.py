'''reducer.py'''
import sys

curr_label = None
curr_count = 0
curr_encod = 0
label = None

for line in sys.stdin:
    label, encod = line.strip().split('\t', 1)
    label, encod = int(label), eval(encod)

    dim = len(encod)
    # 如果当前类别与之前的类别不同，则上一个类别计数完成
    if curr_label != label:
        if curr_label is not None:
            # 求平均数
            print(f'{curr_label}\t{[curr_encod[i] / curr_count for i in range(dim)]}')
        curr_label = label
        curr_count = 0
        curr_encod = [0] * dim
    curr_count += 1
    curr_encod = [curr_encod[i] + encod[i] for i in range(dim)]

# 最后一类
if curr_label == label:
    # 求平均数
    print(f'{curr_label}\t{[curr_encod[i] / curr_count for i in range(dim)]}')