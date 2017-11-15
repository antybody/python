import urllib2
import urllib
values = {"username":"435612413@qq.com","password":"xxx"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
user_agent = 'Mozilla/4.0(compatible;MSIE 5.5; Winodws NT)'
headers = {"User-Agent":user_agent}
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
print response.read()