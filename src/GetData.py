#-*- coding:utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
from tqdm import tqdm
import numpy as np
import requests

def CheckContainChinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

github_site = "https://github.com/"
repository = "pytorch/pytorch/"
label_site = "labels"
issue_site = "issues"
max_page_num = 100
dataset = {}

print("获取repo中所有的issue类别")
for i in tqdm(range(1, max_page_num + 1)):
    # 请求获取HTML
    html = requests.get(github_site + repository + label_site + f'?page={i}')

    # 用BeautifulSoup解析html
    obj = bf(html.text, 'html.parser')

    # 获取本页面所有label
    label_list = obj.find_all(name='div', attrs={'class':'js-label-list'})[0]
    for x in label_list.contents:
        if isinstance(x, str):
            continue
        
        label_name = ''.join(x.span.contents)
        if label_name.find('module') != -1:
            dataset[label_name] = []

    # 判断Next Page是否存在
    if len(obj.find_all(name='a', attrs={'class':"next_page"})) == 0:
        break

print(f"爬取的类别个数：{len(dataset)}")
print('爬取所有issue类别的标题')
for issue_label in tqdm(dataset):
    print("正在爬取类别 " + issue_label + " 的标题")
    # 请求获取对应类别的HTML
    for i in tqdm(range(1, max_page_num + 1)):
        if issue_label.find(' ') != -1:
            html = requests.get(github_site + repository + issue_site + f'?page={i}&q=label:\"' + issue_label.replace(" ", "%20")  + "\"+is:closed")
        else:
            html = requests.get(github_site + repository + issue_site + f'?page={i}&q=label:' + issue_label + "+is:closed")
        # 用BeautifulSoup解析html
        obj = bf(html.text, 'html.parser')
        
        # 预防得不到结果
        issue_list = obj.find_all(name='div', attrs={'aria-label':"Issues"})
        if len(issue_list) == 0:
            break

        # 获取本页面所有issue标题
        issue_list = issue_list[0].contents[1]
        
        for x in issue_list.contents:
            if isinstance(x, str):
                continue

            title_content = ''.join(x.a.contents)
            if CheckContainChinese(title_content) is False:
                dataset[issue_label].append(title_content)
        
        # 判断Next Page是否存在
        if len(obj.find_all(name='a', attrs={'class':"next_page"})) == 0:
            break
    print("类别 " + issue_label + " 的标题数为" + f"{len(dataset[issue_label])}")

np.save("raw_data.npy", dataset)