from utils.dao import db_connector
from tqdm import *

db = db_connector.get_connection()  # 连接数据库


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
    for article in tqdm(articles):
        # if len(articles[article]['abstract']) > 0:  # 如果文章有摘要
        #     abstracts.append(articles[article]['abstract'])
        # else:
        #     abstracts.append("Null")
        abstracts.append(articles[article]['abstract'])
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


# 获取所有作者名 list
def get_all_name_en():
    return db.bupt.list_collection_names()

# TODO:数据库完成后待修改
# 获取该作者的全部文章的引用次数，返回一个 list
def get_all_citation_per_person(name_en):
    cite_list = []
    collection = db.bupt[name_en]
    articles = collection.find().skip(2)[0]['Article']
    for article in tqdm(articles):
        cite_list.append(articles[article]['citation'])
    return cite_list

# TODO:数据库完成后待修改
# 获取该作者的分别是全部文章的第几作者，返回一个 list
def get_all_author_rank_per_person(name_en):
    author_ranks = []
    collection = db.bupt[name_en]
    articles = collection.find().skip(2)[0]['Article']
    for article in tqdm(articles):
        author_ranks.append(articles[article]['author_rank'])
    return author_ranks



# 获取当前作者在每篇文章中是第几作者，类型为dict {rank：作者排名},并将数据存入数据库中的article中
def get_author_rank_dict(name_en, pid):
    collection = db.bupt[name_en]
    articles = collection.find().skip(2)[0]['Article']
    rank_dict = {}
    for article in articles:
        if pid in articles[article]['author']:
            rank_dict[article] = articles[article]['author'].index(pid) + 1
    collection.update_one(
        {"name": name_en},
        {
            '$set': {"author_rank": rank_dict.values()}
        }
    )
    print("更新author_rank成功")

if __name__ == '__main__':
#    get_author_rank_dict("Anfu Zhou", "65/9612")
    get_all_abs_per_person("Anfu Zhou")
