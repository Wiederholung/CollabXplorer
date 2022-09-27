import db_connetor

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
    collection = client.bupt[name_en]
    collection.insert_one(pub)
    print("插入pub成功")


def update_abstract(name_en, abstract, url):
    collection = client.bupt[name_en]
    collection.update_one(
        {"url": url},
        {
            '$set': {"abstract": abstract}
        }
    )
    print("更新abstract成功")
