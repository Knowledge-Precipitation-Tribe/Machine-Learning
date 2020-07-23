# -*- coding: utf-8 -*-#
'''
# Name:         wineClassification
# Description:  
# Author:       super
# Date:         2020/7/23
'''
import pandas as pd
import graphviz
import matplotlib.pyplot as plt

from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

def load_data():
    wine = load_wine()
    # print(wine.data.shape)
    win_data = pd.concat([pd.DataFrame(wine.data), pd.DataFrame(wine.target)], axis=1)
    # print(win_data.head())

    x_train, x_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3)
    return x_train, y_train, x_test, y_test


def build_model():
    clf = tree.DecisionTreeClassifier(criterion="entropy")
    return clf

def plot_tree(model):
    feature_name = ['酒精', '苹果酸', '灰', '灰的碱性', '镁', '总酚', '类黄酮', '非黄烷类酚类', '花青素', '颜 色强度', '色调', 'od280/od315稀释葡萄酒',
                    '脯氨酸']
    dot_data = tree.export_graphviz(model,
                                     feature_names=feature_name,
                                     class_names=["琴酒","雪莉","贝尔摩德"],
                                     filled=True,
                                     rounded=True)
    graph = graphviz.Source(dot_data)
    graph.save("graph.png")

if __name__ == '__main__':

    x_train, y_train, x_test, y_test = load_data()
    model = build_model()
    model.fit(x_train, y_train)
    score = model.score(x_test, y_test)
    print(score)

    plot_tree(model)