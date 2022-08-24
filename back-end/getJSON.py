import json

from pymongo import MongoClient
import math
import random


# 获取作者信息，只接受单一参数
def get_auth_info(id, name_ch, name_en, category):
    if id is not None:
        for col in db.list_collection_names():
            res = db[col].find_one({'id': id})
            if res is not None:
                return res
        return None
    if name_ch is not None:
        for col in db.list_collection_names():
            res = db[col].find_one({'name': name_ch})
            if res is not None:
                return res
        return None
    if name_en is not None:
        for col in db.list_collection_names():
            if col == name_en:
                return db[col].find_one()
        return None
    if category is not None:
        # TODO: 按学院分类
        return None
    return None


def get_data(id=None, name_ch=None, name_en=None, category=None):
    final_json = {'nodes': [], 'links': [], 'categories': []}
    # nodes = ['id', 'name', 'symbolSize', 'x', 'y', 'value', 'category', 'type']
    # links = ['source', 'target', 'value']
    # TODO: demo中categories只有三种，后续需要再添加学院
    categories = [{"name": "计算机学院"}, {"name": "数字媒体与设计艺术学院"}, {"name": "其他"}]
    index = None
    var = 1

    # 添加固定的种类数至finalJson['categories']
    final_json['categories'].append(categories)

    # 获取中心作者个人信息
    auth_info = get_auth_info(id, name_ch, name_en, category)
    # print(auth_info)
    if auth_info is None:
        print('没有找到相关作者信息，请检查参数是否正确！')
        return None

    # 将中心作者添加至finalJson['nodes']
    final_json['nodes'].append(
        # {'id': auth_info['id'], 'name': auth_info['name'], 'symbolSize': 30, 'x': 0, 'y': 0, 'value': 0,
        #  'category': auth_info['category'], 'type': 'node'}
        {'id': auth_info['id'], 'name': auth_info['name'], 'symbolSize': 60, 'x': 0, 'y': 0, 'value': 0,
         'category': 0, 'type': 'node'}
    )

    # 获取中心作者所在的collection
    for col in db.list_collection_names():
        if db[col].find_one({'id': auth_info['id']}) is not None:
            index = col
            break

    # 遍历中心作者的所有合作者
    while db[index].find_one({'相关老师' + str(var): {'$gte': "0"}}) is not None:
        # 获取合作信息
        res = db[index].find({}, {'_id': 0, '相关老师' + str(var): 1, '相关文献:' + str(var): 1}).limit(1).skip(1)
        # 获取合作者信息
        co_auth_info = get_auth_info(None, None, res[0]['相关老师' + str(var)], None)
        # TODO: 目前，如果合作者不隶属BUPT，则跳过
        if co_auth_info is not None:
            # 添加合作者信息至finalJson['nodes']
            # final_json['nodes'].append(
            #     {'id': co_auth_info['id'], 'name': co_auth_info['name'], 'symbolSize': 60, 'x': 0, 'y': 0,
            #      'value': int(res[0]['相关文献:' + str(var)]), 'category': co_auth_info['category'], 'type': 'node'})
            final_json['nodes'].append(
                {'id': co_auth_info['id'], 'name': co_auth_info['name'], 'symbolSize': 60, 'x': 0, 'y': 0,
                 'value': int(res[0]['相关文献:' + str(var)]), 'category': 0, 'type': 'node'})
            # 添加合作信息至finalJson['links']
            final_json['links'].append(
                {'source': auth_info['id'], 'target': co_auth_info['id'], 'value': int(res[0]['相关文献:' + str(var)])})
        var += 1
        # print(res[0])
        # 继续遍历下一段合作关系

    # 动态赋予x y值
    # 代码功能

    # 静态变量
    r = 200  # 半径
    angle = 360  # 角度
    interval = []  # 存储角度数组
    range = []  # 存储xy数据
    numCategory = len(final_json['categories'])  # 获取总共种类数
    numData = len(final_json['nodes'])  # 获取数据个数

    # 计算平均角度，放入interval中
    average = angle / numCategory  # 计算平均角度
    i = 0  # 进行循环赋值
    while i < numCategory:
        angleNow = int(i * average)
        interval.append(angleNow)
        i += 1
    # print(interval)

    # 计算x与y的具体值
    i = 1  # 进行循环赋值（从1开始跳过自己
    while i < numData:
        category = final_json['nodes'][i]["category"]  # 学院是哪个
        randomNum = random.randint(interval[category], interval[category] + 119)  # 生成随机数
        x = r * math.cos(randomNum * 2 * math.pi / 360)
        y = r * math.sin(randomNum * 2 * math.pi / 360)

        # 将xy值添加至finalJson中
        final_json['nodes'][i]['x'] = x
        final_json['nodes'][i]['y'] = y

        i += 1
    return final_json


if __name__ == '__main__':
    client = MongoClient('mongodb://rwAll:ARS 5111-rwAll'
                         '@dev.metattri.com:27017')
    db = client.bupt

    # TODO: 目前finalJson['categories']为空
    # TODO: 判断是传入JSON文件 还是直接以JSON格式直接进行文本传递

    # 需要指定中心作者的id、name_ch、name_en中的一个，以下三种方式皆可
    finalJson = get_data(name_ch="丰雷")  # 演示：假设中心作者为“丰雷”老师
    # finalJson = get_data(id="101")
    # finalJson = get_data(name_en="Lei_Feng_0001")

    # 将finalJson字典转化为json，utf-8编码
    dict_json = json.dumps(finalJson, ensure_ascii=False)
    with open('file.json', 'w+', encoding="utf-8") as file:
        file.write(dict_json)

    print(finalJson['nodes'])
    print(len(finalJson['nodes']))
    print(finalJson['links'])
    print(len(finalJson['links']))
