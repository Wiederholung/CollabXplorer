from DB import db_connetor

client = db_connetor.get_connection()


# 获取作者全部文章摘要
def get_abstract(name_en):
    collection = client.bupt[name_en]
    abstracts = []
    for i in collection.find():
        abstracts.append(i['abstract'])
    return abstracts
