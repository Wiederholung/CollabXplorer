from gensim.models import Word2Vec
import codecs
import pymysql
import numpy
import Utils.articleUtils as articleUtils

numpy.set_printoptions(suppress=True)

fcoms = codecs.open('coms_all.txt', 'r', encoding="utf8")
w2v_model = Word2Vec.load('wiki.zh.1.6gr.model')
w = codecs.open('vec_all.txt', 'w', encoding="utf8")
size = 300  # 词向量维度


def count_vec_sentence():
    # TODO: 读取一个作者的文本内容，计算每个文章的向量，写入vec_all.txt
    line = fcoms.readline()
    i = 0
    id = 0
    while line:
        words = articleUtils.stemmer(line)  # 通过stemmer分词
        vec = numpy.zeros(size).reshape((1, size))
        vec0 = numpy.zeros(size).reshape((1, size))
        count = 0
        flag = True
        for item in words:
            word = item.strip()
            if word.__len__() > 0:
                if flag:
                    attitude = word
                    flag = False
                else:
                    try:
                        vec += w2v_model[word].reshape((1, size))
                        count += 1
                    except KeyError:
                        # print('==== fault: ', word)
                        continue
        if i % 100 == 0:
            print(i)
        i += 1
        line = fcoms.readline()
        if count != 0:
            vec /= count
            w.write(attitude + ' ')
            w.write(str(vec)[2:-2])
            w.write('$')


if '__main__' == __name__:
    count_vec_sentence()
