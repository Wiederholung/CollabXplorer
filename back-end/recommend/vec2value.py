#利用维基百科将Word2vec训练完成后，就得到了语料库中的相应词的词向量，将评论信息转化为词向量的实质是利用“键值对”的原理，将特定词的词向量取出。将评论中的中文词全部转化为词向量后，整条评论的向量值就是其所有分词向量的平均值。核心代码如下。

from gensim.models import Word2Vec
import codecs
import numpy
import Utils.articleUtils as articleUtils
import Utils.dbFindUtils as dbFindUtils

numpy.set_printoptions(suppress=True)

w2v_model = Word2Vec.load('../res/model/word2vec.txt')  # 加载已经处理好的word2vec模型
w = codecs.open('vec_all.txt', 'w', encoding="utf8")  # 写入结果
size = 300  # 词向量维度


def count_vec_sentence():
    # TODO: 读取一个作者的文本内容，计算每个文章的向量，写入vec_all.txt
    # name_list = dbFindUtils.get_all_name()
    fcoms = dbFindUtils.get_abstract("Anfu_Zhou")
    i = 0
    id = 0
    for line in fcoms:
        words = articleUtils.stemmer(line)  # 通过stemmer分词，为一个list
        vec = numpy.zeros(size).reshape((1, size))  # 0矩阵
        vec0 = numpy.zeros(size).reshape((1, size))
        count = 0
        flag = True
        for word in words:
            if word.__len__() > 0:
                if flag:
                    attitude = word
                    flag = False
                else:
                    try:
                        vec += w2v_model[word].reshape((1, size))  # 词向量相加
                        count += 1
                    except KeyError:
                        # print('==== fault: ', word)
                        continue
        if i % 100 == 0:
            print(i)
        i += 1
        line = fcoms.readline()
        if count != 0:
            vec /= count  # 计算每个文章词向量的平均值
            w.write(attitude + ' ')
            w.write(str(vec)[2:-2])
            w.write('$')


if '__main__' == __name__:
    count_vec_sentence()
