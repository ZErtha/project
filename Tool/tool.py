#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/5 14:28
# @Author  : 泽申
# @File    : tool.py
# @Software: PyCharm

import os


def traverse_directory(root_dir, depth=0, max_depth=2):
    file_list = []  # 用于存储文件列表

    if depth > max_depth:
        return file_list

    for root, dirs, files in os.walk(root_dir):
        if root == root_dir:
            continue
        if "idea" in root or "__pycache__" in root:
            continue

        # 遍历当前目录的子目录
        for dir_name in dirs:
            subdir = os.path.join(root, dir_name)
            # 递归遍历下一层目录，并将返回的文件列表合并到当前文件列表中
            traverse_directory(subdir, depth + 1, max_depth)
            file_list.extend([os.path.join(subdir, file) for file in files])

    return file_list


def find_innermost_files(root_dir):
    file_list = []

    for root, dirs, files in os.walk(root_dir):

        if root == root_dir:
            continue
        if "idea" in root or "__pycache__" in root:
            continue
        file_dict = {
            "parent": "",
            "child": []
        }
        if dirs:
            file_list.append({
                "parent": root,
                "child": [os.path.join(root, d) for d in dirs]
            })

    return file_list
