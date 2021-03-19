# Distributed-System-Final-Project

## 题目
在Github代码仓库中，存在大量已分类（即加上标签）的软件bug。但是，现在的分类标签大都是基于人工添加的，效率比较低。本项目通过爬取大量具有分类标签的Bug，利用MapReduce分布式编程模型，实现分类算法，自动给Bug加上标签。

## 要求
1. 爬取至少1000个具有分类标签的bug；
2. 采用MapReduce实现分类算法；
3. 测试验证算法的准确度；
4. 分析结果并得出结论；
5. 提交源码和报告，压缩后命名方式为：学号_姓名_班级

## 项目文件介绍

- report.pdf 项目实验报告

- dataset 实验中使用的预处理好的数据集
  - original_dataset.txt

- src 实验代码文件夹

  - GetData.py 爬虫文件，用于获取数据
  - DataProcess.py 对文本进行预处理
  - SplitData.py 划分训练集和测试集文件
  - WordCount WordCount相关的MapReduce文件
    - mapper.py 
    - reducer.py

  - Train 训练使用的MapReduce文件夹
    - mapper.py
    - reducer.py
  - Test 测试使用的文件夹
    - Test.py
