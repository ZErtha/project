#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/4 18:43
# @Author  : 泽申
# @File    : configs.py
# @Software: PyCharm

class TestMysqlConfig(object):
    """
    测试使用的MySQL配置
    """

    def __init__(self):
        self.name = "root"
        self.password = "root"
        self.host = "192.168.32.69"
        self.port = "3306"
        self.database = "ruo-vue-pro"

    def connect_database_url(self) -> str:
        """
        返回测试使用的MySQL连接URL
        :return:
        """
        return f"mysql://{self.name}:{self.password}@{self.host}:{self.port}/{self.database}"

    def get_serve_url(self) -> str:
        # 伟
        # serve_url = "http://192.168.31.186"
        # 白
        return "http://192.168.31.150:48080"


class ProduceMysqlConfig(object):
    """
    生产服使用的MySQL配置
    """

    def __init__(self):
        self.name = "root"
        self.password = "123456"
        self.host = "99aiot.cn"
        self.port = "4406"
        self.database = "ruo-vue-pro"

    def connect_database_url(self) -> str:
        """
        返回生产服使用的MySQL连接URL
        :return:
        """
        return f"mysql://{self.name}:{self.password}@{self.host}:{self.port}/{self.database}"

    def get_serve_url(self) -> str:
        return "http://admin1.99aiot.net"
