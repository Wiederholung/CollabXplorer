import torch
from torchtext.vocab import GloVe
from utils import article_utils
from utils.dao import db_utils

GloVe_dim = 300
# 从res/model加载glove模型
glove = GloVe(name='6B', dim=GloVe_dim, cache='res/model')


def get_token(content):
    tokens = article_utils.stemmer(content)
    return tokens


def token2vec(tokens):
    vecs = glove.get_vecs_by_tokens(tokens, lower_case_backup=True)
    return vecs


# 计算每个摘要的词向量集
# TODO: 有待优化
def get_abs_word_vec_set(name_en):
    abstracts = db_utils.get_all_abs_per_person(name_en)
    word_vecs_set = torch.zeros(len(abstracts), GloVe_dim)
    tokens_set = []
    count = 0
    # 遍历每一篇文章摘要
    for abstract in abstracts:
        tokens = get_token(abstract)  # 将摘要分词，得到tokens
        tokens_set.append(tokens)
        word_vecs_set[count] = torch.zeros(len(tokens), GloVe_dim)  # TODO: 有问题
        count += 1
    count = 0
    for tokens in tokens_set:
        word_vecs = token2vec(tokens)  # 获取所有单词的向量
        word_vecs_set[count] = word_vecs
        count += 1
    return word_vecs_set


# 计算每个作者的所有摘要向量
def get_abs_vec_set(name_en):
    count = 0
    abstracts = db_utils.get_all_abs_per_person(name_en)
    abs_vec_set = torch.zeros(len(abstracts), GloVe_dim)
    # 遍历每一篇文章摘要
    for abstract in abstracts:
        tokens = get_token(abstract)  # 将摘要分词，得到tokens
        word_vecs = token2vec(tokens)  # 获取所有单词的向量
        abs_vec = torch.mean(word_vecs, dim=0)  # 将摘要向按行行平均，作为摘要向量
        abs_vec_set[count] = abs_vec  # 将摘要向量作为新的一行，加入集合
        count += 1
    return abs_vec_set


# 计算作者的向量
def get_author_vec(name_en):
    abs_vec_set = get_abs_vec_set(name_en)
    author_vec = torch.mean(abs_vec_set, dim=0)
    return author_vec


# 计算两个作者的相似度
def get_similarity(name_en1, name_en2):
    author_vec1 = get_author_vec(name_en1)
    author_vec2 = get_author_vec(name_en2)
    similarity = torch.cosine_similarity(author_vec1, author_vec2)
    return similarity


if __name__ == '__main__':
    # with open('res/Anfu_Zhou.article.txt', 'a', encoding='utf-8') as f:
    #     f.write('article-' + str(count))
    #     for i in article_vec.tolist():
    #         f.write(' ')
    #         f.write(str(round(i, 8)))
    #     f.write('\n')
    #     count += 1

    # for i in db_utils.get_all_name_en():
    #     # abst = get_abs_vec_set(i)
    #     author = get_author_vec(i)
    #     # print(abst)
    #     print(author)

    res = get_similarity('Anfu_Zhou', "Yonghong_Zhao")
    print("done")
