import urllib.request
from xml.dom.minidom import parse
import db_connetor


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
    # TODO: 获取所有的 publication @王少
    for i in root.getElementsByTagName('title'):
        print(i.firstChild.data)


if __name__ == '__main__':
    for col in get_all_col():
        dblp_id = get_pid(col)
        get_pub(dblp_id)
        break
