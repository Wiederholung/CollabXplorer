from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk


# nltk.download("stopwords")
# nltk.download("punkt")
# 去除标点符号，返回值为一个列表

def punctuation(content):
    content.lower()
    cutwords1 = word_tokenize(content)  # 分词
    interpunctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']  # 定义标点符号列表
    cutwords2 = [word for word in cutwords1 if word not in interpunctuations]  # 去除标点符号
    return cutwords2


# 词干提取,返回值为一个列表
def stemmer(content):
    content.lower()
    cutwords1 = word_tokenize(content)  # 分词
    # print('【NLTK分词结果：】')
    # print(cutwords1)
    interpunctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']  # 定义符号列表
    cutwords2 = [word for word in cutwords1 if word not in interpunctuations]  # 去除标点符号
    stops = set(stopwords.words("english"))
    cutwords3 = [word for word in cutwords2 if word not in stops]  # 判断分词在不在停用词列表内
    cutwords4 = []
    for cutword in cutwords3:
        cutwords4.append(PorterStemmer().stem(cutword))  # 词干提取
    return cutwords4


# 测试
if __name__ == '__main__':
    print(stemmer(
        "The first time I heard that song was in Hawaii on radio. I was just a kid, and loved it very much! What a "
        "fantastic song!"))
