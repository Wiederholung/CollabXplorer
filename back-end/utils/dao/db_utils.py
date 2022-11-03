from utils.dao import db_connetor

db = db_connetor.get_connection()  # 连接数据库


# 插入 pub 到个人 document
def insert_pub(name_en, pub):
    try:
        col = db.bupt[name_en]
        col.insert_one(pub)
        print("插入 {}: pub 成功".format(name_en))
    except Exception as e:
        print('[\n错误：{}\n函数：{}\n]'.format(e, insert_pub.__name__))


# 更新 pid 到个人 document
def update_pub(name_en, pid):
    collection = db.bupt[name_en]
    collection.update_one(
        {"category": "计算机学院（国家示范性软件学院）"},
        {
            '$set': {"pid": pid}
        }
    )
    print("更新pid成功")


# 更新 abstract 到个人 document
def update_abstract(name_en, abstract, url):
    collection = db.bupt[name_en]
    collection.update_one(
        {"url": url},
        {
            '$set': {"abstract": abstract}
        }
    )
    print("更新abstract成功")


# 获取作者全部文章的摘要
def get_all_abs_per_person(name_en):
    abstracts = []
    collection = db.bupt[name_en]
    articles = collection.find().skip(2)[0]['Article']
    for article in articles:
        if len(articles[article]['abstract']) > 0:  # 如果文章有摘要
            abstracts.append(articles[article]['abstract'])
        else:
            abstracts.append("Null")
    return abstracts


# 获取作者信息，只接受单一参数
def get_auth_info(id_s, name_ch, name_en, category):
    if id_s is not None:
        for col in db.bupt.list_collection_names():
            res = db.bupt[col].find_one({'id': id_s})
            if res is not None:
                return res
        return None
    elif name_ch is not None:
        for col in db.bupt.list_collection_names():
            res = db.bupt[col].find_one({'name': name_ch})
            if res is not None:
                return res
        return None
    elif name_en is not None:
        for col in db.bupt.list_collection_names():
            if col == name_en:
                return db.bupt[col].find_one()
        return None
    elif category is not None:
        # TODO: 按学院分类
        return None
    else:
        return None


# 获取所有作者名
def get_all_name_en():
    return db.bupt.list_collection_names()
