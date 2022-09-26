# 本程序为demo版本 后续根据数据库调整


# -*- coding:UTF-8 -*-
import requests
import re
import pymongo


# ##链接数据库
#TODO:填写数据库链接信息


# 获取页面信息
def get_page():
    target = url
    req = requests.get(url=target)
    request = req.text
    return request


# 获取相关老师的论文篇数  返回值为列表数据

# 对应关系为 第一个是本人 后面为相关对应人员
def getpage_number():
    result = get_page()
    paper_numb = re.findall(r'.*sc":"(\S*)"', result)
    return paper_numb


# 获取相关老师的姓名 返回值为列表

# 对应关系为 第一个是本人 后面为相关对应人员
def get_name():
    result = get_page()
    author_name = re.findall(r'.*text":":facet:author:(\S*)"', result)
    return author_name


if __name__ == '__main__':
    db = client.URL_db  # 链接bupt数据库 没有自动创建
    collection = db.user  # 使用user集合 没有自动创建

    # #导出每一个url
    # 限制条件
    queryArgs = {}
    res = collection.find(queryArgs)
    error = 1  # 检测第几个异常

    for i in res:

        try:  # 检测遍历循环

            url = i.get('URL')  # 从数据库中获取每个人的信息
            number = getpage_number()
            teacher_name = i.get('Name')
            teacher_category = i.get('Category')
            teacher_id = i.get('id')
            name = get_name()
            teacher_name_En = name[0]

            # 切换到bupt数据库 建立每个老师的集合    与设计文档对应
            teacher_num = number[0]
            db = client['bupt'][teacher_name_En]
            # 老师的个人信息
            data1 = {"id": teacher_id, "name": teacher_name, "pageNum": teacher_num, "category": teacher_category}
            db.insert_one(data1)

            # 删除关于自己的数据
            name.pop(0)
            number.pop(0)

            j = 1  # 标记 相关老师 j
            data2 = {"realted": []}
            templateName = []
            templatePage = []

            # 遍历整理相关老师信息 bug:名字和篇数数字对应不上。
            for i in name:
                num = str(j)
                templateName.append(name[j - 1])  # 将名字存储到临时 存储列表中
                j += 1
            k = 1  # 标记 相关老师 k
            for i in number:
                num = str(k)
                # data2={"相关老师"+num+":":name[k-1] ,"相关文献:"+num+":":number[k-1]}
                templatePage.append(number[k - 1])
                k += 1
                # 处理人数和篇目数不一样的情况,在篇目数后面对应0进行补齐
            if j > k:
                while j > k:
                    templatePage.append(0)
                    k += 1
            l = 1
            while l < len(templateName):
                tem1 = []
                tem1.append(templateName[l])
                tem1.append(templatePage[l])
                data2["realted"].append(tem1)
                l += 1
                tem1.clear
            # 插入相关信息
            db.insert_one(data2)
            # 建立索引 id name category
            db.create_index([('id', pymongo.ASCENDING)], unique=True)
            db.create_index([('name', pymongo.ASCENDING)])
            db.create_index([('category', pymongo.ASCENDING)])
            error += 1

        except:  # 出现异常后执行代码
            print(f'第{error}个错误')
            error += 1

print('success')
