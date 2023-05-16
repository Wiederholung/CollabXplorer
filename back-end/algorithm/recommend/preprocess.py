import time

import torch
from sklearn.manifold import TSNE
from torchtext.vocab import GloVe

from utils import article_utils
from utils.dao import db_utils

# TODO：维度设置为100？
Lambda = 0.56  # 超参数，用于计算每篇文章的权重
beta = 0.5  # 超参数，用于权衡 s_{ij}（prompt的影响力） 和 E_{ij}（学者自身的影响力） 的重要性
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


# 计算学者i对于论文j的贡献度E_Rij,返回一个list
def get_E_Rij(name_en):
    """
    计算老师分别对自己的论文j的贡献度E_Rij_list
    :param name_en:
    :return: 返回一个E_Rij的list
    """
    # 从数据库中读取作者的全部文章的作者数列表X_ij_list
    X_ij_list = db_utils.get_all_authorNum_per_person(name_en)  # TODO：写一个函数，从数据库中读取作者的全部文章的作者数列表X_ij_list
    # 从数据控中读取作者在每篇文章中的排名K_ij_list
    K_ij_list = db_utils.get_all_rank_per_person(name_en)  # TODO：写一个函数，从数据库中读取作者在每篇文章中的排名K_ij_list
    # E_Rij_list用于保存每个E_Rij
    E_Rij_list = []

    # 计算E_Rij:E_{Rij}= \begin{cases} e,& \text{k = 1} \\ e^{\frac{x_{ij}-k}{x_{ij}}}, & \text{others} \end{cases}
    for i in range(len(X_ij_list)):
        if K_ij_list[i] == 1:
            # torch.exp(1.0)表示e
            E_Rij = torch.exp(torch.tensor(1.0))
        else:
            E_Rij = torch.exp((X_ij_list[i] - K_ij_list[i]) / X_ij_list[i])
        E_Rij_list.append(E_Rij)
    return E_Rij_list


# 计算学者i的论文j的影响力E_Cij,返回一个list
def get_E_Cij(name_en):
    """
    计算该老师的论文j的影响力E_Cij_list
    :param name_en:该作者的姓名
    :return:返回一个E_Cij的list
    """
    # 从数据库中获取该作者的全部文章的引用次数列表
    cite_list = db_utils.get_all_citation_per_person(name_en)
    # ni_max是cite_list中的最大值
    ni_max = max(cite_list)
    # E_Cij_list用于保存每个E_Cij
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

    return E_Cij_list


# 计算每个作者的向量，A_i
def get_author_vec(name_en):
    """
    计算每个每个作者的向量A_i(只考虑作者排名和引用次数)
    :param name_en:
    :return: 学者i的向量A_i
    """
    count = 0
    abstract_list = db_utils.get_all_abs_per_person(name_en)
    # cite函数，计算E_Cij
    Cite_list = get_E_Cij(name_en)
    # Contribution函数，计算E_Rij
    Contribution_list = get_E_Rij(name_en)
    abs_vec_set = torch.zeros(len(abstract_list), GloVe_dim).to(device)

    # 遍历每一篇文章摘要
    for abstract in abstract_list:
        tokens = get_token(abstract)  # 将摘要分词，得到tokens
        word_vecs = token2vec(tokens)  # 获取所有单词的向量
        abs_vec = torch.mean(word_vecs, dim=0)  # 将单词按行平均，作为摘要向量

        E_ij = (Lambda * Contribution_list[count] + (1 - Lambda) * Cite_list[count])
        abs_vec = E_ij * abs_vec
        abs_vec_set[count] = abs_vec  # 将摘要向量作为新的一行，加入集合
        count += 1
    A_i = torch.mean(abs_vec_set, dim=0)
    return A_i


# 计算每个作者的被prompt影响后向量，A_i_prompt
def get_author_vec_with_prompt(name_en, prompt):
    """
    计算每个作者的被prompt影响后向量A_i_prompt
    :param name_en: 想要被查询的作者的姓名
    :param prompt: 从前端获取的prompt
    :return: A_i_prompt：被prompt影响后的学者
    """
    # TODO: 从前端获取prompt
    tokens = get_token(prompt)  # 将摘要分词，得到tokens
    prompt_vecs = token2vec(tokens)  # 获取所有单词的向量
    prompt_vec = torch.mean(prompt_vecs, dim=0)  # 将单词按行平均，作为摘要向量
    # 计数器
    count = 0
    abstract_list = db_utils.get_all_abs_per_person(name_en)
    # cite函数，计算E_Cij
    Cite_list = get_E_Cij(name_en)
    # Contribution函数，计算E_Rij
    Contribution_list = get_E_Rij(name_en)
    abs_vec_set = torch.zeros(len(abstract_list), GloVe_dim).to(device)

    # 遍历每一篇文章摘要
    for abstract in abstract_list:
        tokens = get_token(abstract)  # 将摘要分词，得到tokens
        word_vecs = token2vec(tokens)  # 获取所有单词的向量
        abs_vec = torch.mean(word_vecs, dim=0)  # 将单词按行平均，作为摘要向量

        # 计算得到论文 j 与 prompt 的 similarity s_{ij}
        s_ij = torch.cosine_similarity(abs_vec, prompt_vec, dim=0)
        # 变换s_ij的值域，s'_{ij} = \frac{e-1}{2}(s_{ij}+1) + 1
        s_ij = (torch.exp(torch.tensor(1.0)) - 1) / 2 * (s_ij + 1) + 1
        E_ij = (Lambda * Contribution_list[count] + (1 - Lambda) * Cite_list[count])
        # 计算学者 i 的论文 j 的权重 W_{ij}，W_{ij} = \beta s'_{ij} + (1-\beta)E_{ij}
        W_ij = beta * s_ij + (1 - beta) * E_ij
        # 计算由 prompt 调制后的学者 A_i’，A_i’ = \frac{\sum_{j=1}^{m} W_{ij} \vec{P_{ij}}}{m}
        abs_vec = W_ij * abs_vec
        abs_vec_set[count] = abs_vec  # 将摘要向量作为新的一行，加入集合
        count += 1
    A_i_prompt = torch.mean(abs_vec_set, dim=0)
    return A_i_prompt


# 计算中心学者U与学者A_i的推荐度 suitability S_i
def get_suitability(central_scholar_name, target_scholar_name, prompt):
    """
    计算中心学者与学者A_i的 suitability S_i
    :param central_scholar_name:
    :param target_scholar_name:
    :param prompt:
    :return: 中心学者关于目标学者的推荐度S_i
    """
    # 获取中心学者的向量
    central_scholar_vec = get_author_vec(central_scholar_name)
    # 获取目标学者的向量
    target_scholar_vec = get_author_vec_with_prompt(target_scholar_name, prompt)
    # 计算中心学者U与学者A_i的 suitability S_i
    S_i = torch.cosine_similarity(central_scholar_vec, target_scholar_vec, dim=0)
    return S_i


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
    torch.save(all_sim, 'res/all_sim-' + str(GloVe_dim) + 'd.pt')


if __name__ == '__main__':
    # v = get_author_vec('Anfu_Zhou')
    # res = get_similarity('Anfu_Zhou', "Anlong_Ming")
    # a = get_author_vec_set()
    # get_2d_vec(a)
    write_sim()
    print("done")
