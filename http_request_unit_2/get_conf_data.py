#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/20/2018 3:46 PM
# @Author  : yimi
# @File    : get_conf_data.py

import configparser

class GetConfigData:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path

    def get_conf_data(self, section, option):
        cf = configparser.ConfigParser()
        cf.read(self.config_file_path)
        value = cf.get(section, option)
        return value

if __name__ == "__main__":
    value = GetConfigData("ip.conf").get_conf_data("IP", "ip")
    print(value)