import numpy as np

label_list = [
    'module: cuda',
    'module: nn',
    'module: autograd',
    'module: tests',
    'module: internals',
    'module: bc-breaking',
    'module: build',
    'module: flaky-tests',
    'module: third_party',
    'module: binaries'
    ]

class_proto = {}
with open("result3") as fp:
    lines = fp.readlines()
    for line in lines:
        label, proto = line.strip().split('\t', 1)
        class_proto[int(label)] = np.array(eval(proto))

# (total, accuracy)
stat = {x : [0,0] for x in label_list}
with open("TestDataset") as fp:
    for line in fp.readlines():
        label_idx, test_vec, sentence = line.strip().split('\t', 2)
        label_idx, test_vec = int(label_idx), np.array(eval(test_vec))

        dist = []
        max_dist, max_label = -np.inf, None
        for u, v in class_proto.items():
            curr_dist = np.dot(test_vec, v)/(np.linalg.norm(test_vec)*(np.linalg.norm(v)))
            dist.append(curr_dist)
            
            if curr_dist > max_dist:
                max_dist, max_label = curr_dist, u

        label = label_list[label_idx]
        # 判断测试是否正确
        if max_label == label_idx:
            stat[label][1] += 1
        print(f'{label} {dist[label_idx]} | {label_list[max_label]} {dist[max_label]} | {sentence}')
        stat[label][0] += 1

for u, v in stat.items():
    print(f'{u} | Total: {v[0]} | Accuracy: {v[1]} | Acc rate: {v[1] / v[0]}')