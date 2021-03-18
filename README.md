# Distributed-System-Final-Project

项目文件介绍

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