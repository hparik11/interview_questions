#!/usr/bin/env python
# coding:utf-8
"""
@FileName : flipping_image.py
@Author   : Harsh Parikh
@Date     : 10/2/21 5:52 PM

832. Flipping an Image
Easy

1640

193

Add to List

Share
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].


Example 1:

Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
"""


class Solution:
    def flipAndInvertImage(self, image):

        def reverse_list(alist):
            n = len(alist)
            i = 0
            while i < n // 2:
                alist[i], alist[n - i - 1] = alist[n - i - 1], alist[i]

                i += 1

        for i in range(len(image)):
            reverse_list(image[i])
            for j in range(len(image[i])):
                image[i][j] = image[i][j] ^ 1

        return image
