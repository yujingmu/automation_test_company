#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/14/2018 11:03 AM
# @Author  : yimi
# @File    : run.py

import time
import unittest
import HTMLTestRunnerNew
from http_request_unit_3.test_http_request import TestHttpRequest
from http_request_unit_3.logger import Logger
from http_request_unit_3.send_emal import SendEmail

logger = Logger('api_test_logger', 'DEBUG', 'DEBUG')

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

day_time = time.strftime("%Y-%m-%d")


with open("test_result-"+day_time+".html", "wb+") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, title='ddt_api test', description=None, tester='yimi')
    runner.run(suite)
logger.info("finished testing and generated test report")

subject = '薏米的测试报告'
sender = '1281018605@qq.com'
receiver = '1281018605@qq.com'
mail_text = 'api test result(logging and sendemal)'
mail_attach = "test_result-"+day_time+".html"
auth_code = 'pxqswpbzogoohahbqqqq'
SendEmail(subject, sender, receiver, mail_text, mail_attach, auth_code).send_email()
