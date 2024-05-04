#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/3 2:48 PM
# @Author  : sunwenjun
# @File    : crawl_news_title.py
# @brief: 爬取网站上新闻标题  http://www.hxnews.com

import requests
from bs4 import BeautifulSoup


def crawl_news_title(url, drop_txt):
    text_list = []
    try:
        r = requests.get(url, timeout=600)  # 10分钟后还没有返回结果，就不在请求
    except requests.exceptions.RequestException as e:
        print(e)

    r.encoding = None
    result = r.text
    bs = BeautifulSoup(result, 'html.parser')
    pages = bs.find_all('ul', {"class": "newlistbox"})  # 获取下面的页码
    for page in pages:
        a_list = page.find_all('a')
        for a in a_list:
            text = a.text.strip()
            if text == drop_txt or len(text) == 0:
                # print(url, text)
                continue
            text_list.append(text)
    return text_list


def process(root, page_start, page_end, outfile, drop_txt):
    text_list = []
    for num in range(page_start, page_end):
        url = root + str(num) + ".shtml"
        text_list += crawl_news_title(url, drop_txt)
        if num % 100 == 0:
            print(url)

    with open(outfile, 'w', encoding='utf-8') as f:
        for s in text_list:
            f.write(s + "\n")
    return


if __name__ == '__main__':
    root = "http://www.hxnews.com/news/gn/gnxw/"
    outfile = './国内新闻.txt'
    drop_txt = "国内新闻"
    process(root=root, page_start=1, page_end=2, outfile=outfile, drop_txt=drop_txt)
    print("done")
