import urllib2

request = urllib2.Request('http://blog.csdn.net/cqcre123')
try:
    urllib2.urlopen(request)
except urllib2.URLError,e:
    print e.reason
except urllib2.HTTPError,e:
    print e.code
else:
    print "OK"