            #本程序为demo版本 后续根据数据库调整


# -*- coding:UTF-8 -*-
from cgitb import reset, text
from unicodedata import name
from unittest import result
import requests
import re

#该部分为获取写入数据库的URL（每个老师的
url=""

#获取页面信息 之后完善
def get_page():
    
    target = 'https://dblp.org/search/publ/api?callback=jQuery31107668076119769278_1648782955416&q=author%3AXiuqin_Lin%3A&compl=author&p=2&h=0&c=21&format=jsonp&_=1648782955418'
    req = requests.get(url=target)
    request=req.text
    return request


# 获取相关老师的论文篇数  返回值为列表数据

    #对应关系为 第一个是本人 后面为相关对应人员
def getpage_number():
    
    result=get_page()
    paper_numb=re.findall(r'.*sc":"(\S)"',result)
    return paper_numb
    

#获取相关老师的姓名 返回值为列表

    #对应关系为 第一个是本人 后面为相关对应人员
def get_name():
    
    result=get_page()
    author_name=re.findall(r'.*text":":facet:author:(\S*)"',result)
    return author_name

#遍历导出数据
    


if __name__ == '__main__':
    number=getpage_number()
    name=get_name()
    print(number)
    print(name)
    # print(req.text)