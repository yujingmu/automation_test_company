#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/14/2018 11:03 AM
# @Author  : yimi
# @File    : run.py

import time
import unittest
import HTMLTestRunnerNew
from http_request_unit_2.test_http_request import TestHttpRequest

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

day_time = time.strftime("%Y-%m-%d")

print(day_time)

with open("test_result-"+day_time+".html", "wb+") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, title='ddt_api test', description=None, tester='yimi')
    runner.run(suite)

