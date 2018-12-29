#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/28/2018 4:22 PM
# @Author  : yimi
# @File    : logger.py
import logging
import time
import os

class Logger:
    def __init__(self, logger_name, logger_level, logfile_level):
        self.logger_name = logger_name
        self.logger_level = logger_level
        self.logfile_level = logfile_level

    def logger(self, msg, level):
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(self.logger_level)    # 包含DEBUG级别在内以上的日志
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-logging info:%(message)s')
        now_time = time.strftime('%Y-%m-%d')
        path = "api_test_result-"+now_time+".txt"
        file_log = logging.FileHandler(path, encoding='UTF-8')     # 输出到指定文件  encoding='UTF-8'
        file_log.setLevel(self.logfile_level)
        file_log.setFormatter(formatter)
        logger.addHandler(file_log)
        if level.upper() == 'DEBUG':
            logger.debug(msg)
        elif level.upper() == 'INFO':
            logger.info(msg)
        elif level.upper() == 'WARNING':
            logger.warning(msg)
        elif level.upper() == 'ERROR':
            logger.error(msg)
        elif level.upper() == 'CRITICAL':
            logger.critical(msg)
        logger.removeHandler(file_log)          # 解决日志重复问题

    def debug(self, msg):
            self.logger(msg, 'DEBUG')
    def info(self, msg):
            self.logger(msg, 'INFO')
    def warning(self, msg):
            self.logger(msg, 'WARNING')
    def error(self, msg):
            self.logger(msg, 'ERROR')
    def critical(self, msg):
            self.logger(msg, 'CRITICAL')

if __name__ == '__main__':
    logger_name1 = 'api_test_logger'
    logger_level1 = 'DEBUG'
    logfile_level1 = 'DEBUG'
    logger = Logger(logger_name1, logger_level1, logfile_level1)
    logger.debug("debug 信息")

