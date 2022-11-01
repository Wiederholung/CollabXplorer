# 将glove转化为word2vec格式的示例文件

from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec

glove_file = '../res/model/glove.6B.300d.txt'  # 下载好的Glove模型
tmp_file = "../res/model/word2vec.txt"  # 希望转换到的目标文件
# _ = glove2word2vec(glove_file, tmp_file)   # 开始转换

glove2word2vec(glove_file, tmp_file)
# model = KeyedVectors.load_word2vec_format(tmp_file, binary=False)

model = KeyedVectors.load_word2vec_format(tmp_file)  # 读取新的模型文件

# 获得单词cat的词向量
cat_vec = model['cat']
print(cat_vec)
# 获得单词frog的最相似向量的词汇
print(model.most_similar('frog'))
