import urllib.request
from xml.dom.minidom import parse
from DB import db_connetor
from crawler import IEEE

# 获取 db 内所有 collection 的名字
def get_all_col():
    db = db_connetor.get_connection().bupt
    return db.list_collection_names()


def get_xml(url):
    return parse(urllib.request.urlopen(url))


def get_pid(name_en):
    url = 'https://dblp.uni-trier.de/search/author?xauthor=' + name_en
    xml = get_xml(url)
    root = xml.documentElement
    return root.getElementsByTagName('author')[0].getAttribute('pid')


def get_pub(pid):
    url = 'https://dblp.org/pid/' + pid + '.xml'
    xml = get_xml(url)
    root = xml.documentElement
    # TODO: 获取所有需要的 publication 信息 @王少
    for i in root.getElementsByTagName('title'):
        print(i.firstChild.data)
    # a_list = root.getElementsByTagName('article')
    # a_url = a_list[2].getAttribute('ee').getFirstChild().data
    # IEEE.get_abstract(a_url)


# TODO: 获取所有需要的 abstract 信息 @胡 @川泽
def get_abstract(url):
    pass


if __name__ == '__main__':
    # TODO: 将 pid 写入数据库 @川泽

    # TODO: 将 pub 写入数据库 @川泽

    # TODO: 将 abstract 写入数据库 @川泽
    for col in get_all_col():
        dblp_id = get_pid(col)
        get_pub(dblp_id)
        break
