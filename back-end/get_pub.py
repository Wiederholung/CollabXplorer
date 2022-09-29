import json
import urllib.request
from xml.dom.minidom import parse
import DB.Utils.updateUtils as updateUtils
import crawler.crawlerUtils


def get_xml(url):
    try:
        response = urllib.request.urlopen(url)
        xml_root = parse(response).documentElement
    except Exception as e:
        print('[\n错误：{}\n函数：{}\n]'.format(e, get_xml.__name__))
        xml_root = ''
    return xml_root


def get_pid(name_en):
    url = 'https://dblp.uni-trier.de/search/author?xauthor=' + name_en
    root = get_xml(url)
    try:
        pid = root.getElementsByTagName('author')[0].getAttribute('pid')
    except IndexError as e:
        print('错误：{}，未找到 pid：{}'.format(e, name_en))
        pid = ''
    except Exception as e:
        print('[\n错误：{}\n函数：{}\n]'.format(e, get_pid.__name__))
        pid = ''
    return pid


def get_dblp_pub(pid):
    url = 'https://dblp.org/pid/' + pid + '.xml'
    xml = get_xml(url)
    return xml


def xml_browser(xml):
    # 获取根节点
    root = xml
    try:
        # 最终返回的字典
        result = {'id': root.getAttribute('pid'), 'name': root.getAttribute('name'), 'Article': {}}

        # 获取合作者信息，遍历每个合作文章
        # 获取 inproceedings 节点
        in_proceedings = root.getElementsByTagName('inproceedings')
        for paper in in_proceedings:
            result = paper_manager(paper, result)
        # 获取 articles 节点
        articles = root.getElementsByTagName('article')
        for paper in articles:
            result = paper_manager(paper, result)
    except Exception as e:
        print('[\n错误：{}\n函数：{}\n]'.format(e, xml_browser.__name__))
        result = ''
    return result


# 处理每一个 paper 节点，article 和 in_proceeding
def paper_manager(paper, result):
    # 获取key值
    article_name = paper.getAttribute('key')
    result['Article'][article_name] = {}
    # 获取title
    try:
        result['Article'][article_name]['title'] = paper.getElementsByTagName('title')[0].childNodes[0].data
    except Exception as e:
        print(e)
        result['Article'][article_name]['title'] = ''
    # 获取url
    try:
        result['Article'][article_name]['url'] = paper.getElementsByTagName('ee')[0].childNodes[0].data
    except Exception as e:
        print(e)
        result['Article'][article_name]['url'] = ''
    # 获取year
    try:
        result['Article'][article_name]['year'] = paper.getElementsByTagName('year')[0].childNodes[0].data
    except Exception as e:
        print(e)
        result['Article'][article_name]['year'] = ''
    # 获取合作者
    result['Article'][article_name]['author'] = {}
    for i in range(0, len(paper.getElementsByTagName('author'))):
        try:
            result['Article'][article_name]['author'][paper.getElementsByTagName('author')[i].childNodes[0].data] = \
                paper.getElementsByTagName('author')[i].getAttribute('pid')
        except Exception as e:
            print(e)
            result['Article'][article_name]['author'][
                paper.getElementsByTagName('author')[i].childNodes[0].data] = ''
    # 获取摘要
    try:
        result['Article'][article_name]['abstract'] = crawler.crawlerUtils.get_abstract(
            result['Article'][article_name]['url'])
    except Exception as e:
        print(e)
        result['Article'][article_name]['abstract'] = ''
    # print(result['Article'][article_name])
    return result


if __name__ == '__main__':
    # 从 Shao-yong_Gao 继续
    for col in updateUtils.get_all_col()[68:]:
        # 获取 pid
        dblp_id = get_pid(col)
        # 根据 pid 获取 dblp_pub_xml
        dblp_xml = get_dblp_pub(dblp_id)
        # 解析 xml 并添加摘要，得到格式化后的字典
        json_dict = xml_browser(dblp_xml)
        # 将字典格式化为 json
        json_str = json.dumps(json_dict, ensure_ascii=False)
        # 将 json 写入文件
        with open('res/dblp/' + col + '.json', 'w', encoding='utf-8') as f:
            f.write(str(json_str))
        # 将 json 写入数据库
        updateUtils.insert_pid(col, json_dict)

    # xml = parse('Shao-Yong_Guo.xml')
    # json_dict = xml_browser(xml.documentElement)
    # json_str = json.dumps(json_dict, ensure_ascii=False)
