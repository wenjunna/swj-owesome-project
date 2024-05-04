#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/9 2:47 PM
# @Author  : sunwenjun
# @File    : extract_useful_sents.py
# @brief: 判断一个句子是否包含有效信息

import re


class ExtractUsefulSents(object):
    def __init__(self):
        pass

    def extract_useful_chars(self, txt):
        '''
        提取中英文字母，朝鲜语，日语,其实还有其他语言例如俄语，藏语
        返回字符串
        '''
        text = txt.lower()
        pattern = re.compile(
            "[A-Za-z\u4e00-\u9fa5\u3040-\u318F\u1100-\u11FF\uAC00-\uD7AF]+")  #
        res = re.findall(pattern, text)
        res = "".join(res)
        return res

    def is_useful(self, txt="哈哈哈"):
        '''
        判断一句话是否包含有效信息
        :param txt: 文本
        :return:有效返回"0",True
        '''
        tmp = self.extract_useful_chars(txt)
        tmp2 = list(set(list(tmp)))

        # 1，如果没有有效字符，判断为无效句子
        if not tmp:
            return "1", False

        # 2，去重之后的字母和汉字，长度小于2，则视为无效句子
        if len(tmp2) < 2:
            return "2", False

        # 3，提取出的字母和汉字，占原有字符串长度不足1/10，则视为无效句子
        if len(tmp) / len(txt) < 0.1:
            return "3", False

        # 4，重复3遍以上，且丰富度小于等于5，视为无效句子
        if len(tmp2) / len(tmp) < 0.33 and len(tmp2) < 6:
            return "4", False

        return "0", True


if __name__ == '__main__':
    txt_list = ["。。。。。", "12345", "qqqqq", "🇦🇹", "哈哈哈哈～～～", "简单简单简单简单", "暂时不考虑新的机会！暂时不考虑新的机会！暂时不考虑新的机会！"]
    myfilter = ExtractUsefulSents()
    for txt in txt_list:
        sign, flag = myfilter.is_useful(txt)
        print(sign, flag, txt)
