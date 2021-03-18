import numpy as np 
from tqdm import tqdm
import re

def TextProcess(raw_text):
    # Keep Only English Text
    comp = re.compile('[^A-Z^a-z ]')
    
    # lower
    res = comp.sub(' ', raw_text).lower()

    return res

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
dataset = np.load("raw_data.npy", allow_pickle=True).item()

text_processed = {}
for i in range(10):
    res = []

    cur_label = label_list[i]
    for x in dataset[cur_label]:   
        res.append(TextProcess(x))
    text_processed[cur_label] = res

fp = open("original_dataset.txt", 'w')
for i in tqdm(range(10)):
    cur_label = label_list[i]
    for x in tqdm(text_processed[cur_label]):
        fp.write(cur_label + '\t' + x + '\n')

fp.close()