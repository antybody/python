#-*-coding:utf-8-*-
"""
 descript 练习 Requests
"""
import requests

r = requests.get('http://cuiqingcai.com')
print type(r)
print r.status_code
print r.encoding
print r.cookies
