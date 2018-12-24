#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/14/2018 10:45 AM
# @Author  : yimi
# @File    : test_http_request.py

from http_request_unit_1.http_request import HttpRequest
from http_request_unit_1.get_test_data import GetTestData
import unittest

class TestHttpRequest(unittest.TestCase):

    def __init__(self, methodName, url, param, method, expected, case_id, mode, case_id_list):
        super(TestHttpRequest, self).__init__(methodName)
        self.url = url
        self.param = param
        self.method = method
        self.expected = expected
        self.case_id = case_id
        self.mode = mode
        self.case_id_list = case_id_list

    def setUp(self):
        self.session = HttpRequest()
        self.data = GetTestData("test_data.xlsx", self.mode, self.case_id_list)

    def test_login(self):
        res = self.session.http_request(self.url, self.param, self.method)
        self.data.write_data(self.case_id+1, 7, "data", str(res))
        try:
            self.assertEqual(eval(self.expected), res)
            result = "Pass"
        except AssertionError as e:
            print("断言错误， 错误信息为：{0}".format(e))
            result = "Fail"
            raise e
        finally:
            self.data.write_data(self.case_id + 1, 8, "data", result)

    def tearDown(self):
        None
