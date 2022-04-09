            #本程序为demo版本 后续根据数据库调整


# -*- coding:UTF-8 -*-
from cgitb import reset, text
from unicodedata import name
from unittest import result
import requests
import re

# ##链接数据库
from pymongo import MongoClient
client =MongoClient("metattri.com",27017)

    



#获取页面信息 
def get_page():
    
    target = url
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



if __name__ == '__main__':
    db=client.URL_db#链接bupt数据库 没有自动创建
    collection = db.user#使用user集合 没有自动创建

    # #导出每一个url
    #限制条件
    queryArgs = {}
    projectionFields = ['URL']
    res=collection.find(queryArgs,projectionFields)
    
    for i in res:
        error=1 #检测第几个异常
        
        try:# 检测遍历循环
            
            url=i.get('URL')    #从数据库中获取每个人的url
            number=getpage_number()
            name=get_name()
            
            
                #切换到bupt数据库 建立每个老师的集合    与设计文档对应
            teacher_name=name[0]
            teacher_num=number[0]
            db=client['bupt'][teacher_name]
                #老师的个人信息
            data1 = { "个人论文篇数" : teacher_num }
            db.insert_one(data1)
            
            #删除关于自己的数据
            name.pop(0)
            number.pop(0)
            j=1 #标记 相关老师 j
            data2 = {}
            
                # 遍历整理相关老师信息 bug:名字和篇数数字对应不上。
            for i in name:
                num=str(j)
                data2[ "相关老师"+num]=name[j-1]
                j+=1
            k=1 #标记 相关老师 k
            for i in number:
                num=str(k)
                data2["相关文献"+num]= number[k-1]
                k+=1
                
                #插入相关信息
            db.insert_one(data2)
            error+=1
            
        except:#出现异常后执行代码
            print(f'第{error}个错误')
            error+=1
            
print('success')
