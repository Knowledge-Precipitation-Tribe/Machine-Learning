# -*- coding: utf-8 -*-#
'''
# Name:         em
# Description:  EM算法应用于王者荣耀数据分类
# Author:       super
# Date:         2020/6/4
'''

# -*- coding: utf-8 -*-
import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

import warnings
warnings.filterwarnings('ignore')


def load_data():
    # 数据加载，避免中文乱码问题
    data_ori = pd.read_csv('../data/em_data/heros.csv', encoding='gb18030')
    features = [u'最大生命', u'生命成长', u'初始生命', u'最大法力', u'法力成长', u'初始法力', u'最高物攻', u'物攻成长', u'初始物攻', u'最大物防', u'物防成长',
                u'初始物防',
                u'最大每5秒回血', u'每5秒回血成长', u'初始每5秒回血', u'最大每5秒回蓝', u'每5秒回蓝成长', u'初始每5秒回蓝', u'最大攻速', u'攻击范围']
    data = data_ori[features]
    plt_headmap(data, features)

    # 相关性大的属性保留一个，因此可以对属性进行降维
    features_remain = [u'最大生命', u'初始生命', u'最大法力', u'最高物攻', u'初始物攻', u'最大物防', u'初始物防', u'最大每5秒回血', u'最大每5秒回蓝',
                       u'初始每5秒回蓝',
                       u'最大攻速', u'攻击范围']
    data = data_ori[features_remain]
    data[u'最大攻速'] = data[u'最大攻速'].apply(lambda x: float(x.strip('%')) / 100)
    data[u'攻击范围'] = data[u'攻击范围'].map({'远程': 1, '近战': 0})

    return data_ori, data


def plt_headmap(data, features):
    # 对英雄属性之间的关系进行可视化分析
    # 设置plt正确显示中文
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # 用热力图呈现features_mean字段之间的相关性
    corr = data[features].corr()
    plt.figure(figsize=(14, 14))
    # annot=True显示每个方格的数据
    sns.heatmap(corr, annot=True)
    plt.show()


def build_model(data):
    # 构造GMM聚类
    gmm = GaussianMixture(n_components=30, covariance_type='full')
    return gmm


if __name__ == '__main__':
    data_ori, data = load_data()

    # 采用Z-Score规范化数据，保证每个特征维度的数据均值为0，方差为1
    ss = StandardScaler()
    data = ss.fit_transform(data)

    gmm = build_model(data)
    gmm.fit(data)
    # 训练数据
    prediction = gmm.predict(data)
    print(prediction)
    # 将分组结果输出到CSV文件中
    data_ori.insert(0, '分组', prediction)
    data_ori.to_csv('./hero_out.csv', index=False, sep=',')