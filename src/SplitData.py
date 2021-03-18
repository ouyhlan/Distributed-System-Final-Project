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

label_dict = {
    'module: cuda' : 0,
    'module: nn' : 1,
    'module: autograd' : 2,
    'module: tests' : 3,
    'module: internals' : 4,
    'module: bc-breaking' : 5,
    'module: build' : 6,
    'module: flaky-tests' : 7,
    'module: third_party' : 8,
    'module: binaries' : 9
}

vocab2idx = {}
idx2vocab = []
vocab_stat = {}
with open("part-00000",'r') as fp:
    for i, line in enumerate(fp.readlines()):
        word, count = line.strip().split('\t', 1)
        vocab_stat[word] = int(count)
        vocab2idx[word] = i
        idx2vocab.append(word)

dataset = {x:[] for x in range(len(label_list))}
with open('original_dataset.txt', 'r') as fp:
    lines = fp.readlines()
    
    # 计算所有词语IDF值
    doc_num = len(lines)
    vocab_idf = np.zeros(len(idx2vocab))

    for i in range(len(idx2vocab)):
        vocab_idf[i] = np.log2(doc_num / (vocab_stat[idx2vocab[i]] + 1))

    for i, line in enumerate(lines):
        encod = np.zeros(len(idx2vocab))
        label, sentence = line.strip().split('\t', 1)

        # 将句子分割为词
        words = sentence.split()

        # 分割为<word, 1>
        for word in words:
            encod[vocab2idx[word]] += 1
        
        # 计算TF值
        encod /= len(words)

        # 计算TF-IDF值
        encod *= vocab_idf

        dataset[label_dict[label]].append((encod, sentence))

fp_train, fp_test = open('TrainDataset', 'w'), open('TestDataset', 'w')
for label, sentences in dataset.items():
    train_num = int(len(sentences) * 0.8)
    for x in sentences[:train_num]:
        fp_train.write(f'{label}\t{x[0].tolist()}\n')

    for x in sentences[train_num:]:
        fp_test.write(f'{label}\t{x[0].tolist()}\t{x[1]}\n')

fp_train.close(), fp_test.close()
