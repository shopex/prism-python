# __author__ = 'daixinyu'
#coding=utf8

a = {1: 1, 2: 2, 3: 3}
b = a.copy()
b[4] = 4
print b, a

print len("123")
import urllib

m = {'par': "哈哈", }
print urllib.urlencode(m)

print urllib.quote("client_id=buwb2lii&sign_method=md5&sign_time=1409550675")