#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/25/2018 5:29 PM
# @Author  : yimi
# @File    : send_emal.py

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart    # 声明这个邮件是由多部分组成的
from email.mime.application import MIMEApplication

class SendEmail:
    def __init__(self, subject, sender, receiver, mail_text, mail_attach, auth_code):
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.mail_text = mail_text
        self.mail_attach = mail_attach
        self.auth_code = auth_code
        self.msg = MIMEMultipart()

    def send_email(self):
        # msg=MIMEMultipart()
        self.msg['Subject'] = self.subject
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

        # 纯文本邮件体
        msg_text = MIMEText(self.mail_text)
        self.msg.attach(msg_text)

        # 附加的附件xls, html, rar
        msg_attachment = MIMEApplication(open(self.mail_attach, 'rb').read())
        msg_attachment.add_header('Content-Disposition', 'attachment', filename=self.mail_attach)
        self.msg.attach(msg_attachment)

        # 登录服务器
        s = smtplib.SMTP_SSL('smtp.qq.com', 465)
        s.login(self.sender, self.auth_code)  # 账号， 授权码
        s.sendmail(self.sender,self.receiver, self.msg.as_string())
        s.close()


if __name__ == "__main__":
    subject = '薏米的测试报告'
    sender = '1281018605@qq.com'
    receiver = '1281018605@qq.com'
    # receiver = '281417558@qq.com'
    mail_text = 'api test result'
    mail_attach = 'api_test_result.html'
    auth_code = 'pxqswpbzogoohahb'
    SendEmail(subject, sender, receiver, mail_text, mail_attach, auth_code).send_email()