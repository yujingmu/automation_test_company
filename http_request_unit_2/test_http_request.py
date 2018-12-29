#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/14/2018 10:45 AM
# @Author  : yimi
# @File    : test_http_request.py

from http_request_unit_2.http_request import HttpRequest
from http_request_unit_2.get_test_data import GetTestData
from ddt import ddt, data
import unittest
from http_request_unit_2.get_conf_data import GetConfigData

ip = GetConfigData("ip.conf").get_conf_data("IP", "ip")
mode = GetConfigData("ip.conf").get_conf_data("CONFIG", "mode")
case_id_list = GetConfigData("ip.conf").get_conf_data("CONFIG", "case_id_list")
test_data = GetTestData("test_data.xlsx", mode, case_id_list).get_test_data("data")

@ddt
class TestHttpRequest(unittest.TestCase):

    def setUp(self):
        self.session = HttpRequest()
        self.data = GetTestData("test_data.xlsx", mode, case_id_list)

    @data(*test_data)
    def test_login(self, item):
        res = self.session.http_request(ip+item['url'], eval(item['param']), item['method'])
        self.data.write_data(item['case_id']+1, 7, "data", str(res))
        try:
            self.assertEqual(eval(item['expected']), res)
            result = "Pass"
        except AssertionError as e:
            print("断言错误， 错误信息为：{0}".format(e))
            result = "Fail"
            raise e
        finally:
            self.data.write_data(item['case_id'] + 1, 8, "data", result)

    def tearDown(self):
        None
