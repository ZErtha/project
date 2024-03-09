#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/8 11:27
# @Author  : 泽申
# @File    : mkdir.py
# @Software: PyCharm
import os


def mkdir(work_path, dir_name) -> bool:
    """
    创建目录
    :param work_path: 当前运行的文件路径
    :param dir_name: 目录名
    :return:
    """
    dir_path = os.path.join(work_path, dir_name)
    is_exists = os.path.exists(dir_path)

    if not is_exists:
        # 如果不存在，则创建目录
        os.mkdir(dir_path)
        return True
    else:
        # 如果目录存在则不创建
        return False
