# -*- coding: utf-8 -*-#
'''
# Name:         Regression
# Description:  
# Author:       super
# Date:         2020/6/6
'''

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import VotingRegressor

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


def load_data():
    x, y = load_boston(return_X_y=True)
    x = StandardScaler().fit_transform(x)
    y = StandardScaler().fit_transform(y.reshape(-1, 1))
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state = 42)
    return (x_train, y_train), (x_test, y_test)



if __name__ == '__main__':
    (x_train, y_train), (x_test, y_test) = load_data()

    model1 = LinearRegression(n_jobs=-1)
    model2 = RandomForestRegressor(n_estimators=10, random_state=1, n_jobs=-1)
    model3 = LinearRegression(n_jobs=-1)
    model = VotingRegressor(estimators=(['model1', model1],
                                        ['model2', model2],
                                        ['model3', model3]))
    model.fit(x_train, y_train)

    print(model.score(x_test, y_test))