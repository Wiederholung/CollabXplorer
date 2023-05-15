import time

import torch
from sklearn.manifold import TSNE
from torchtext.vocab import GloVe

from utils import article_utils
from utils.dao import db_utils

# TODO：维度设置为100？
Lambda = 0.56  # 超参数，用于计算每篇文章的权重
GloVe_dim = 300
# 从res/model加载glove模型
glove = GloVe(name='6B', dim=GloVe_dim, cache='res/model')
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")  # 使用 CUDA
print(device)


def get_token(content):
    tokens = article_utils.stemmer(content)
    return tokens


def token2vec(tokens):
    vecs = glove.get_vecs_by_tokens(tokens, lower_case_backup=True).to(device)
    return vecs


# 计算E_Cij,返回一个list
def get_E_Cij(cite_list):
    """
    计算E_Cij
    :param cite_list:
    :return:
    """
    # ni_max是cite_list中的最大值
    ni_max = max(cite_list)
    E_Cij_list = []

    # 遍历cite_list，每一个元素是n_ij，如果n_ij>0，那么C_ij=1，如果n_ij=0，那么C_ij=0
    for n_ji in cite_list:
        if n_ji > 0:
            C_ij = 1
        else:
            C_ij = 0
        # 计算E_Cij：E_{Cij} = C_{ij} e^{\frac{n_{ij}}{n_{i_{max}}}}
        E_Cij = C_ij * torch.exp(C_ij / ni_max)
        # 使用E_Cij_list保存每个E_Cij
        E_Cij_list.append(E_Cij)

    return E_Cij


# 计算每个作者的所有摘要向量
def get_author_vec(name_en):
    """
    计算每个每个作者的向量
    :param name_en:
    :return:
    """
    # TODO: 从数据库中读取作者的每一篇文章的影响因子参数（引用数）和贡献度（第几作者）
    count = 0
    abstract_list = db_utils.get_all_abs_per_person(name_en)
    Cite_list = db_utils.get_all_cite_per_person(name_en) #TODO 写一个cite函数，计算E_Cij
    Contribution_list = db_utils.get_all_contribution_per_person(name_en) #TODO 写一个Contribution函数，计算E_Rij
    abs_vec_set = torch.zeros(len(abstract_list), GloVe_dim).to(device)
    # 遍历每一篇文章摘要
    for abstract in abstract_list:
        tokens = get_token(abstract)  # 将摘要分词，得到tokens
        word_vecs = token2vec(tokens)  # 获取所有单词的向量
        abs_vec = torch.mean(word_vecs, dim=0)  # 将单词按行平均，作为摘要向量
        E_ij = (Lambda * Contribution_list[count] + (1- Lambda ) * Cite_list[count])
        abs_vec = E_ij * abs_vec
        abs_vec_set[count] = abs_vec  # 将摘要向量作为新的一行，加入集合
        count += 1
    return torch.mean(abs_vec_set, dim=0)

# TODO: 推荐算法（根据Prompt，重新计算作者向量）



# 计算作者的向量
# def get_author_vec(name_en):
#     abs_vec_set = get_abs_vec_set(name_en)
#     author_vec = torch.mean(abs_vec_set, dim=0)
#     #  将 author_vec 转置，变成行向量
#     # author_vec = author_vec.unsqueeze(0)
#     return author_vec


# 计算作者的向量集
def get_author_vec_set():
    author_set = db_utils.get_all_name_en()
    author_vec_set = torch.zeros(len(author_set), GloVe_dim).to(device)
    for i in range(len(author_set)):
        author_vec_set[i] = get_author_vec(author_set[i]).unsqueeze(0)
        print(author_vec_set[i])
    torch.save(author_vec_set, 'res/author_vec_set.pt')
    return author_vec_set


# 通过TSNE将向量降到2维
def get_2d_vec(vec_set):
    x = vec_set.numpy()
    x_embedded = TSNE(n_components=2).fit_transform(x)
    torch.save(x_embedded, 'res/author_vec_set-2d.pt')
    return x_embedded


# 计算两个作者的相似度，返回值为0-1之间的浮点数
def get_similarity(name_en1, name_en2):
    author_vec1 = get_author_vec(name_en1).unsqueeze(0)
    author_vec2 = get_author_vec(name_en2).unsqueeze(0)
    similarity = torch.cosine_similarity(author_vec1, author_vec2)
    return similarity.item()


def write_sim():
    all_name = db_utils.get_all_name_en()
    all_sim = torch.zeros(len(all_name), len(all_name)).to(device)
    for i in range(len(all_name)):
        start = time.time()  # 开始计时
        vec_i = get_author_vec(all_name[i]).unsqueeze(0)
        j = i
        print(all_name[i] + " start")
        while j < len(all_name):
            vec_j = get_author_vec(all_name[j]).unsqueeze(0)
            all_sim[i][j] = torch.cosine_similarity(vec_i, vec_j)
            print(all_sim[i][j])
            j += 1
        print(all_name[i] + " cost: " + str(time.time() - start))  # 计时结束
    # 将tensor写入文件
    torch.save(all_sim, 'res/all_sim-'+str(GloVe_dim)+'d.pt')


if __name__ == '__main__':
    # v = get_author_vec('Anfu_Zhou')
    # res = get_similarity('Anfu_Zhou', "Anlong_Ming")
    # a = get_author_vec_set()
    # get_2d_vec(a)
    write_sim()
    print("done")
