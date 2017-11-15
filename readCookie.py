#encoding:UTF-8
import cookielib
import urllib2

#创建MozillaCookie
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie 到变量
cookie.load("cookie.txt",ignore_expires=True,ignore_discard=True)
#创建请求的request
req = urllib2.Request("http://www.baidu.com")
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()