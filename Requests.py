#-*-coding:utf-8-*-
"""
 descript 练习 Requests
"""
import requests
import json

r = requests.get('http://cuiqingcai.com')
print type(r)
print r.status_code
print r.encoding
print r.cookies

print u"-----------------带参数的请求-------------"
payload = {'key1':'values'}
r1 = requests.get("http://httpbin.org/get",params=payload)
print r1.url

print u"-----------------请求json文件-------------"

r2 = requests.get("http://127.0.0.1:8020/html5/data.json")
print r2.text
print r2.json()

print u"---------------POST请求------------------"
url = "http://httpbin.org/post"
r3 = requests.post(url,data=json.dumps(payload))
print r3.text

print u"-------------上传文件---------------"
file = {'file':open('cookie.txt','rb')}
r4 = requests.post(url,files=file)
print r4.text

print u"------------更新cookie------------"
url = "http://httpbin.org/cookies"
cookies = dict(cookies_are='working')
r5 = requests.get(url,cookies=cookies)
print r5.text

print u"---------长久会话--------------"
s = requests.session()
s.headers.update({'x-test':'true'})
r6 = s.get("http://httpbin.org/headers",headers={'x-test1':'true'})
print r6.text

print u"------------SSL证书验证------------"
r7 = requests.get("https://github.com",verify=True)
print r7.text
