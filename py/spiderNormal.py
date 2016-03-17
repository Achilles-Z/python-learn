#!/usr/bin/python
# -*- coding: utf-8 -*-
#author zeck.tang 2016.03.03

"""
文件头两行注释是用于避免文件中包含中文导致如下错误
SyntaxError: Non-ASCII character XXX in file xxx.py on line xx, but no encoding declared
see http://python.org/dev/peps/pep-0263/ for details
如果遇到
IndentationError: unexpected indent
这样的错误,请仔细检查每个空格和tab
"""

import urllib
import urllib2
import re

# 这个是百度手机助手里面优酷的用户评论的信息获取url,咱是用Charles抓包拿到的 
# ps:这个只有第一页数据,可以改写下动态传入pn参数值获取后续页面的信息
url = 'http://shouji.baidu.com/comment?action_type=getCommentList&groupid=3528441&pn=1'

# UserAgent设置 如果有需要UA的话
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#headers = { 'User-Agent' : user_agent }
try:
	# UA塞进头里
    #request = urllib2.Request(url,headers = headers)
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8') # utf-8格式读出来避免乱码
    # 可以先打印看看content内容然后看怎么写正则
    # print content 
    
    # content内容非常规则,每个<li></li>包含一条评论信息内容 
    # <em>(.*?)</em>是用户名称
    # <p>(.*?)</p>是评论内容
    # <div.*?time">(.*?)</div>是评论时间
    pattern = re.compile('<em>(.*?)</em>.*?<p>(.*?)</p>.*?<div.*?time">(.*?)</div>',re.S)
    items = re.findall(pattern,content)
    for item in items:
		#打印每一条评论
		print item[0] #用户名称
		print item[1] #用户评论
		print item[2] #评论时间
		print "----------"
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    else :
		print "code else"
    if hasattr(e,"reason"):
        print e.reason
    else:
    	print "reason else"

