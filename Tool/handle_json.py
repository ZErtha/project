#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/8 11:27
# @Author  : 泽申
# @File    : handle_json.py
# @Software: PyCharm
import json


def get_data(data_path) -> json:
    """
    获取文件，json格式
    :param data_path:
    :return:
    """
    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def save_json(file_path, data_json):
    """
    保存为json文件
    :param file_path:
    :param data_json:
    :return:
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data_json, f, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行
