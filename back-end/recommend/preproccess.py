import torch
from torchtext.vocab import GloVe
from utils import articleUtils, dbFindUtils

# 从res/model加载glove模型
glove = GloVe(name='6B', dim=300)


def get_token(content):
    tokens = articleUtils.stemmer(content)
    return tokens


def get_vec(tokens):
    ret = glove.get_vecs_by_tokens(tokens, lower_case_backup=True)
    return ret


if __name__ == '__main__':
    count = 1
    for abstract in dbFindUtils.get_abstract("Anfu_Zhou"):
        token = get_token(abstract)
        abs_vec = get_vec(token)
        article_vec = torch.mean(abs_vec, dim=0)
        with open('../res/model/Anfu_Zhou.article.txt', 'a', encoding='utf-8') as f:
            f.write('article-' + str(count))
            for i in article_vec.tolist():
                f.write(' ')
                f.write(str(round(i, 8)))
            f.write('\n')
            count += 1
        # print(vec_tensor)
