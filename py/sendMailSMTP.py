#!/usr/bin/python
# -*- coding: utf-8 -*-
#author zeck.tang 2016.03.03
 """
 这个小脚本可以用于自动化报告发送啊,各类什么监控预警邮件啥的
 把邮件正文部分改造成你需要的正文填充就行了
 用起来挺方便,简单好用
 可以扩展下,用于自动化生产html邮件正文或者excel数据表然后发送
 运维,数据部门的小伙伴可以研究下写个脚本用起来
 """
import string
import smtplib
import os
import datetime
import convert2html
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header

today = datetime.date.today()
# 发件人
sender = 'xxx@xx.com'
# 收件人列表
receiverlist = ["x1@x1.com","x2@x2.com"]
# 邮件标题
subject = '%s %s' % ('python邮件发送脚本test',today)
# SMTP邮件服务器地址
smtpserver = 'smtp.exmail.qq.com'
# 发件人的邮箱账号
username = 'xxx@xx.com'
# 发件人的邮箱密码 其实账号密码可以通过input形式
password = 'xx'

# 邮件正文内容
f = open('index.html',"r")
content = f.read()
#msg = MIMEText(content,'html','utf-8')
msg = MIMEMultipart()
# 邮件正文设置utf-8 和 格式指定html
msg.attach(MIMEText(content,'html','utf-8'))
# from指定
msg['From'] = 'xxx@xx.com'
# 正文指定
msg['Subject'] = subject
# 添加文件名称为index.html的文件作为附件
att=MIMEText(open('index.html','rb').read(),'base64','gb2312')
att["Conten-Type"]='application/octet-stream'
att["Content-Disposition"]='attachment;filename="index.html"'
msg.attach(att)
# init SMTP
smtp = smtplib.SMTP()
# 连接服务器
smtp.connect(smtpserver)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
# 账号密码登录
smtp.login(username, password)
# 发送邮件,第一个参数是发件人,第二个参数是收件人,第三个是邮件正文内容
smtp.sendmail(msg['From'],receiverlist,msg.as_string())
# 打完收工:)
smtp.quit()