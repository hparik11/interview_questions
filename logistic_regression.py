#!/usr/bin/env python
# coding:utf-8
"""
@FileName : logistic_regression.py
@Author   : Harsh Parikh
@Date     : 6/27/21 11:45 PM
"""

import numpy as np


class LogisticRegression:

    def __init__(self, lr=0.01, n_iter=200):
        self.lr = lr
        self.n_iter = n_iter
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iter):
            linear_model = np.dot(X, self.weights) + self.bias
            y_predicted = self._sigmoid(linear_model)
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_predicted = self._sigmoid(linear_model)
        y_predicted_class = [1 if i > 0.5 else 0 for i in y_predicted]
        return y_predicted_class


if __name__ == '__main__':
    log_reg = LogisticRegression()
    X = np.array([[1, 2, 1], [4, 2, 2], [1, 2, 1], [1, 2, 3], [1, 4, 1]])
    y = np.array([0, 1, 1, 0, 1])

    log_reg.fit(X, y)
    print(log_reg.predict(X))
