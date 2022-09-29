from DB import db_connetor

client = db_connetor.get_connection()


# 数据库更新工具类

# 更新pid到个人document
def update_pid(name_en, pid):
    collection = client.bupt[name_en]
    collection.update_one(
        {"category": "计算机学院（国家示范性软件学院）"},
        {
            '$set': {"pid": pid}
        }
    )
    print("更新pid成功")


# 插入pub到个人document
def insert_pid(name_en, pub):
    try:
        collection = client.bupt[name_en]
        collection.insert_one(pub)
        print("插入 {}: pub 成功".format(name_en))
    except Exception as e:
        print('[\n错误：{}\n函数：{}\n]'.format(e, insert_pid.__name__))


def update_abstract(name_en, abstract, url):
    collection = client.bupt[name_en]
    collection.update_one(
        {"url": url},
        {
            '$set': {"abstract": abstract}
        }
    )
    print("更新abstract成功")


def get_all_col():
    db = db_connetor.get_connection().bupt
    return db.list_collection_names()


if __name__ == '__main__':
    data1 = {
        "id": 92,
        "Article": {
            "aid2": {"title": "学科推荐系统2", "author": {"王俊翔": "02/2100", "王伊哲": "02/2100"},
                     "url": "https://doi.org/10.1109/COMPSAC54236.2022.00123", "year": 2100, "abstract": "xxxxxx"},
            "aid1": {"title": "学科推荐系统1", "author": {"朱子炫": "02/2100", "胡逸同": "02/2100"},
                     "url": "https://dblp.org/pid/65/9612.xml", "year": 2100, "abstract": "xxxxxx"}
        }
    }
    insert_pid("Anfu_Zhou", data1)
