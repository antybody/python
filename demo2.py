# encoding: utf-8  
import urllib2
import cookielib
# 一个 cookie 对象
cookie = cookielib.CookieJar()
# 利用 urllibs
handle = urllib2.HTTPCookieProcessor(cookie)
# 通过handle来构建opener
opener = urllib2.build_opener(handle)
# 此处的open 方法 用 urlopen 一样
response = opener.open("http://www.baidu.com")
for item in cookie:
    print 'Name ='+item.name
    print 'Value = '+ item.value