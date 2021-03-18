'''reducer.py'''
import sys

curr_word = None
curr_count = 0
word = None

for line in sys.stdin:
    # 输入格式 <word, count>
    word, count = line.strip().split('\t', 1)

    count = int(count)
    # 如果当前词与之前的词不同，则上一个单词计数完成
    if curr_word != word:
        if curr_word is not None:
            print(f'{curr_word}\t{curr_count}')
        curr_word = word
        curr_count = 0
    curr_count += count

# 最后一类词
if curr_word == word:
    print(f'{curr_word}\t{curr_count}')