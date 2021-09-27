#!/usr/bin/env python
# coding:utf-8
"""
@FileName : get_statistics.py
@Author   : Harsh Parikh
@Date     : 9/2/21 4:19 PM
"""

from collections import Counter
import math


def find_mean(array):
    if not array:
        return 0
    return sum(array) / len(array)


def find_median(array):
    array.sort()

    if len(array) % 2:
        return array[len(array) // 2]
    else:
        return (array[len(array) // 2] + array[(len(array) // 2) - 1]) / 2


def find_mode(array):
    return Counter(array).most_common()[0][0]


def find_sample_variance(array):
    mean = find_mean(array)
    return sum([((x - mean) ** 2) / (len(array) - 1) for x in array])


def find_sample_standard_deviation(array):
    return math.sqrt(find_sample_variance(array))


def find_population_variance(array):
    mean = find_mean(array)
    return sum([((x - mean) ** 2) / len(array) for x in array])


def find_population_standard_deviation(array):
    return math.sqrt(find_population_variance(array))


def find_confidence_interval(array):
    mean = find_mean(array)
    sample_standard_deviation = find_sample_standard_deviation(array)

    mean_standard_error = sample_standard_deviation / math.sqrt(len(array))

    z_score = 1.96  # for 95 percentile
    z_score_standard_error = z_score * mean_standard_error

    return [mean - z_score_standard_error, mean + z_score_standard_error]


def get_statistics(input_list):
    # Write your code here.
    return {
        "mean": find_mean(input_list),
        "median": find_median(input_list),
        "mode": find_mode(input_list),
        "sample_variance": find_sample_variance(input_list),
        "sample_standard_deviation": find_sample_standard_deviation(input_list),
        "mean_confidence_interval": find_confidence_interval(input_list),
    }
