#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/14/2018 10:34 AM
# @Author  : yimi
# @File    : http_request.py

import requests
from http_request_unit_3.logger import Logger

logger = Logger('api_test_logger', 'DEBUG', 'DEBUG')

COOKIES = None
class HttpRequest:

    def http_request(self, url, param, method):

        global COOKIES
        if method.upper() == "GET":
            try:
                res = requests.get(url, params=param, cookies=COOKIES)
            except Exception as e:
                logger.error("get请求出错了， 错误信息为{0}".format(e))
                raise e
        elif method.upper() == "POST":
            try:
                res = requests.post(url, params=param, cookies=COOKIES)
            except Exception as e:
                logger.error("Post请求出错了， 错误信息为{0}".format(e))
                raise e
        else:
            logger.error("请求方法method不正确， 请重新输入method")

        if res.cookies != {}:
            COOKIES = res.cookies

        return res.json()

if __name__ == "__main__":
    login_url = "http://47.107.168.87:8080/futureloan/mvc/api/member/register"
    login_data = {'mobilephone': '18093192866', 'pwd': '123456'}
    session = HttpRequest()
    res = session.http_request(login_url, login_data, method="get")
    print(res)


