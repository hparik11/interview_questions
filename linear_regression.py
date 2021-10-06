import math
from typing import List


# Mean
def mean(values: List):
    return sum(values) / (1.0 * len(values))


def variance(values):
    return sum([(x - mean(values)) ** 2 for x in values]) / (len(values) - 1)


def standard_deviation(values):
    return math.sqrt(variance(values))


def covariance(X, Y):
    return sum([(x - mean(X)) * (y - mean(Y)) for x, y in zip(X, Y)]) / (len(X) - 1)


def find_coefficients_b0_b1(X, Y):
    b1 = covariance(X, Y) / variance(x)
    b0 = mean(y) - mean(x) * b1

    return b0, b1


# Calculate root mean squared error
def rmse_metric(actual, predicted):
    sum_error = 0.0
    for i in range(len(actual)):
        prediction_error = predicted[i] - actual[i]
        sum_error += (prediction_error ** 2)
    mean_error = sum_error / float(len(actual))
    return math.sqrt(mean_error)


def simple_linear_regression(train, test):
    predictions = []
    x_train = [row[0] for row in train]
    y_train = [row[1] for row in train]

    b0, b1 = find_coefficients_b0_b1(x_train, y_train)

    for row in test:
        yhat = b0 + b1 * row[0]
        predictions.append(yhat)

    return predictions


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Mean : %.3f" % mean(values))
    print("Variance : %.3f" % variance(values))
    print("Stand Daviation : %.3f" % standard_deviation(values))
    # print(variance(values))
    # print(standard_daviation(values))

    dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
    x = [row[0] for row in dataset]
    y = [row[1] for row in dataset]

    print("Covariance : %.3f" % covariance(x, y))
    b0, b1 = find_coefficients_b0_b1(x, y)
    print('Coefficients: B0=%.3f, B1=%.3f' % (b0, b1))
