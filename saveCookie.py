# encoding: utf-8
import cookielib
import urllib2
# 设置保存cookie的文件,cookie.txt
filename = 'cookie.txt'
# 一个MozillaCookieJar对象示例来保存cookie,之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
# 利用urllibs库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过handler 来构建opener
opener = urllib2.build_opener(handler)
# 创建一个请求,原理同
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True,ignore_expires=True)