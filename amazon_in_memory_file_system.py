# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: amazon_in_memory_file_system.py
# @Date:   10/19/20, Mon
"""
588. Design In-Memory File System

Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

readContentFromFile: Given a file path, return its content in string format.



Example:

Input:
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

Output:
[null,[],null,null,["a"],"hello"]

Explanation:
filesystem
"""

from collections import defaultdict

class FileSystem(object):
    def __init__(self):
        self.trie = {}  # trie tree
        self.fileinfo = defaultdict(str)  # path: content

    def ls(self, path):
        if path in self.fileinfo:
            return path.split('/')[-1:]

        cur = self.trie
        for token in path.split('/'):
            if token in cur:
                cur = cur[token]
            elif token:
                return []

        return sorted(cur.keys())

    def mkdir(self, path):
        cur = self.trie
        for token in path.split('/'):
            if token not in cur:
                cur[token] = {}
            cur = cur[token]

    def addContentToFile(self, filePath, content):
        self.mkdir(filePath)
        self.fileinfo[filePath] += content

    def readContentFromFile(self, filePath):
        return self.fileinfo[filePath]
