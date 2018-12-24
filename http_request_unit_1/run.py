#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/14/2018 11:03 AM
# @Author  : yimi
# @File    : run.py

from http_request_unit_1.test_http_request import TestHttpRequest
import unittest
import HTMLTestRunnerNew
from http_request_unit_1.get_test_data import GetTestData
from http_request_unit_1.get_conf_data import GetConfigData

ip = GetConfigData("ip.conf").get_conf_data("IP", "ip")
mode = GetConfigData("ip.conf").get_conf_data("CONFIG", "mode")
case_id_list = GetConfigData("ip.conf").get_conf_data("CONFIG", "case_id_list")
test_data = GetTestData("test_data.xlsx", mode, case_id_list).get_test_data("data")

suite = unittest.TestSuite()
for item in test_data:
    print("正在执行第{0}条用例：{1}".format(item["case_id"], item["title"]))
    suite.addTest(TestHttpRequest("test_login", ip+item["url"], eval(item["param"]), item["method"], item["expected"], item["case_id"], mode, case_id_list))

with open("test_result.html", "wb+") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(file)
    runner.run(suite)

