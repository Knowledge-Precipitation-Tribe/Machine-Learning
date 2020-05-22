# -*- coding: utf-8 -*-#
'''
# Name:         text_classification
# Description:  
# Author:       super
# Date:         2020/5/22
'''

import os
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

LABEL_MAP = {'体育': 0, '女性': 1, '文学': 2, '校园': 3}
# 加载停用词
with open('../text_classification_data/stop/stopword.txt', 'rb') as f:
    STOP_WORDS = [line.strip() for line in f.readlines()]


def load_data(base_path):
    """
    :param base_path: 基础路径
    :return: 分词列表，标签列表
    """
    documents = []
    labels = []

    for root, dirs, files in os.walk(base_path): # 循环所有文件并进行分词打标
        for file in files:
            label = root.split('\\')[-1] # 因为windows上路径符号自动转成\了，所以要转义下
            labels.append(label)
            filename = os.path.join(root, file)
            with open(filename, 'rb') as f: # 因为字符集问题因此直接用二进制方式读取
                content = f.read()
                word_list = list(jieba.cut(content))
                words = [wl for wl in word_list]
                documents.append(' '.join(words))
    return documents, labels


def train_fun(td, tl, testd, testl):
    """
    构造模型并计算测试集准确率，字数限制变量名简写
    :param td: 训练集数据
    :param tl: 训练集标签
    :param testd: 测试集数据
    :param testl: 测试集标签
    :return: 测试集准确率
    """
    # 计算矩阵
    tt = TfidfVectorizer(stop_words=STOP_WORDS, max_df=0.5)
    tf = tt.fit_transform(td)
    # 训练模型
    clf = MultinomialNB(alpha=0.001).fit(tf, tl)
    # 模型预测
    test_tf = TfidfVectorizer(stop_words=STOP_WORDS, max_df=0.5, vocabulary=tt.vocabulary_)
    test_features = test_tf.fit_transform(testd)
    predicted_labels = clf.predict(test_features)
    # 获取结果
    x = metrics.accuracy_score(testl, predicted_labels)
    return x


# text classification与代码同目录下
train_documents, train_labels = load_data('../text_classification_data/train')
test_documents, test_labels = load_data('../text_classification_data/test')
x = train_fun(train_documents, train_labels, test_documents, test_labels)
print(x)