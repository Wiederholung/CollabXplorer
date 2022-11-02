from DB import db_connetor

client = db_connetor.get_connection()


# 获取作者全部文章摘要
def get_abstract(name_en):
    abstracts = []
    collection = client.bupt[name_en]
    articles = collection.find().skip(2)[0]['Article']
    for article in articles:
        if len(articles[article]['abstract']) > 0:
            abstracts.append(articles[article]['abstract'])
    return abstracts


# main
if __name__ == '__main__':
    print(get_abstract('Anfu_Zhou'))
