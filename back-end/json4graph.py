from pymongo import MongoClient

client = MongoClient('mongodb://rwAll:ARS 5111-rwAll'
                     '@dev.metattri.com:27017')

db = client.bupt
finalJson = {'nodes': [], 'links': [], 'categories': []}
nodes = ['id', 'name', 'symbolSize', 'x', 'y', 'value', 'category', 'type']
links = ['source', 'target', 'value']
# TODO: categories是什么？
categories = ['name']


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
    index = None
    var = 1

    # 获取中心作者个人信息
    auth_info = get_auth_info(id, name_ch, name_en, category)
    print(auth_info)
    if auth_info is None:
        print('没有找到相关作者信息，请检查参数是否正确！')
        return None

    # 将中心作者添加至finalJson['nodes']
    finalJson['nodes'].append(
        {'id': auth_info['id'], 'name': auth_info['name'], 'symbolSize': 30, 'x': 0, 'y': 0, 'value': 0,
         'category': auth_info['category'], 'type': 'node'})

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
        # TODO: 如果合作者不隶属BUPT，则跳过
        if co_auth_info is not None:
            # 添加合作者信息至finalJson['nodes']
            finalJson['nodes'].append(
                {'id': co_auth_info['id'], 'name': co_auth_info['name'], 'symbolSize': 60, 'x': 0, 'y': 0,
                 'value': int(res[0]['相关文献:' + str(var)]), 'category': co_auth_info['category'], 'type': 'node'})
            # 添加合作信息至finalJson['links']
            finalJson['links'].append(
                {'source': auth_info['id'], 'target': co_auth_info['id'], 'value': int(res[0]['相关文献:' + str(var)])})
        var += 1
        # print(res[0])
        # 继续遍历下一段合作关系


# main函数，假设中心作者为“丰雷”老师
get_data(name_ch="丰雷")

print(finalJson['nodes'])
print(len(finalJson['nodes']))
print(finalJson['links'])
print(len(finalJson['links']))
