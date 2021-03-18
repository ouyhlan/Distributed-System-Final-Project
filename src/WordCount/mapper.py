'''mapper.py'''

import sys

# input comes from STDIN
for line in sys.stdin:
    label, sentence = line.strip().split('\t', 1)

    # 将句子分割为词
    words = sentence.split()

    # 分割为<word, 1>
    for word in words:
        print(f'{word}\t{1}')