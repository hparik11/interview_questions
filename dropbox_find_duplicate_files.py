#!/usr/bin/env python
# coding:utf-8
"""
@FileName : dropbox_find_duplicate_files.py
@Author   : Harsh Parikh
@Date     : 7/18/21 11:24 AM

609. Find Duplicate File in System

Given a list paths of directory info, including the directory path, and all the files with contents in this directory, return all the duplicate files in the file system in terms of their paths. You may return the answer in any order.

A group of duplicate files consists of at least two files that have the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
It means there are n files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content) respectively in the directory "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of groups of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"


Example 1:

Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
Example 2:

Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
"""

"""
Dropbox
Duplicate Files
https://leetcode.com/problems/find-duplicate-file-in-system/
Given a file system, return a list of collections of duplicate files. 
Ask about:
Symbolic link, same file/dir with diff name, cannot detect cycle by visited...cycle?
-use absolute path/ skip symbolic link (if we search the whole file system)
What about invalid or malformed files e.g. permission or cannot read
-compare file by hashing (MD5, SHA)
If dir depth is large: DFS might stack overflow, use BFS; the variable to store pathname might overflow.
-Most memory consuming: MD5, read in files etc
What about race conditions, like if someone is writing the file while you are reading etc
What if the process takes a long time? 
-If error / hanging up in between: checkpoints, save states from time to time
"""

from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for filePath in paths:
            fileNames = filePath.split()
            directoryPath = fileNames[0]
            for file in fileNames[1:]:
                fileSplit = file.split("(")
                fileName, fileContent = fileSplit[0], fileSplit[1].rstrip(')')

                dic[fileContent].append(directoryPath + '/' + fileName)

        duplicateFiles = []

        for value in dic.values():
            if len(value) > 1:
                duplicateFiles.append(value)

        return duplicateFiles


class DuplicateFiles:
    mb = 1024 * 1024

    def __init__(self, root):
        self.result = []
        self.size_to_files = {}
        self.root = root

    def get_hash(self, file):
        """Returns the SHA 256 hash of the file"""
        output_hash = hashlib.sha256()
        with open(file, "rb") as file_obj:
            mb_chunk = file_obj.read(mb)
            if mb_chunk is not None:
                output_hash.update(mb_chunk)
            else:
                return output_hash.hexdigest()
        return output_hash.hexdigest()

    def add_file(self, file):
        if file.file_size in self.size_to_files:
            self.size_to_files[file.file_size].append(file)
        else:
            self.size_to_files[file.file_size] = [file]

    def group_files_by_size(self):
        """Populates self.size_to_files with the sizes and the files with those sizes"""
        queue = collections.deque()
        queue.appendleft(self.root)
        seen = set()
        while queue:
            current_folder = queue.pop()
            seen.add(current_folder)
            for content in current_folder.iter_dir():  # iterdir is the contents of the file, both files and folders
                if content.is_directory() and content not in seen:
                    queue.appendleft(content)
                    seen.add(content)
                elif content.is_file():
                    self.add_file(content)
                else:
                    # Ask the interviewer how to handle symlinks or special cases
                    pass

    def process_files(self):
        """Returns list of collections of duplicate files"""
        # First, group the files by size
        self.group_files_by_size()

        # Now you have the files grouped by size
        # For the sizes with more than one file, you need to deduplicate
        result = []
        for size, files in self.size_to_files.items():
            if len(files) > 1:
                hash_groups = {}  # Map <hash: str, files with that hash: List[File]>
                for file in files:
                    file_hash = self.get_hash(file)
                    if file_hash in hash_groups:
                        hash_groups[file_hash].append(file)
                    else:
                        hash_groups[file_hash] = [file]
                for list_of_files in hash_groups.values():
                    if len(list_of_files) > 1:
                        result.append(list_of_files)
        return result
