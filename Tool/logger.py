#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/7 13:59
# @Author  : 泽申
# @File    : logger.py
# @Software: PyCharm
import logging
import colorlog


class CustomLogger:
    """
    自定义的日志处理器
    """

    def __init__(self, logger_name, log_file_name,
                 log_path="E:/Log",
                 debug_color="white",
                 info_color="green",
                 warning_color="yellow",
                 error_color="red",
                 critical_color="bold_red"):
        self.log_colors_config = {
            'DEBUG': debug_color,
            'INFO': info_color,
            'WARNING': warning_color,
            'ERROR': error_color,
            'CRITICAL': critical_color,
        }

        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        # 设置日志输出格式
        file_formatter = logging.Formatter(
            fmt='[%(asctime)s.%(msecs)03d] %(filename)s -> [%(funcName)s] line:%(lineno)d [%(levelname)s] : %(message)s',
            datefmt='%Y-%m-%d  %H:%M:%S'
        )
        console_formatter = colorlog.ColoredFormatter(
            fmt='%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> [%(funcName)s] line:%(lineno)d [%(levelname)s] : %(message)s',
            datefmt='%Y-%m-%d  %H:%M:%S',
            log_colors=self.log_colors_config
        )

        # 创建控制台日志处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)

        # 创建文件日志处理器
        file_handler = logging.FileHandler(filename=f"{log_path}/{log_file_name}", mode='a',
                                           encoding='utf8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

    def remove_handlers(self):
        for handler in self.logger.handlers[:]:
            handler.close()
            self.logger.removeHandler(handler)
