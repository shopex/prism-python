# __author__ = 'daixinyu'
# coding=utf8
import hashlib
import time
import urllib2
import urllib


class PrismClient:
    def __init__(self, url, key, secret):
        self.url = url
        self.key = key
        self.secret = secret

    def doPost(self, action, params):
        return self.run("POST", action, params)

    def doGet(self, action, params):
        return self.run("GET", action, params)

    def run(self, method, action, params):
        request_params = self.fix_params(action, params)
        print "请求url：%s \t \n" % (self.url)
        print "请求参数:%s \t \n" % (request_params)
        print "请求方式:%s \t \n" % (method)
        try:
            if method == "GET":
                s = ""
                for key, val in request_params.iteritems():
                    s += "%s=%s&" % (key, val)
                response = urllib2.urlopen(self.url + action + "?" + s)
                return response.read()
            elif method == "POST":
                req = urllib2.Request(self.url + action, urllib.urlencode(request_params))
                response = urllib2.urlopen(req)
                return response.read()
        except Exception, e:
            return "[%s] \t %s \t %s \t \n" % (method, self.url, e)

    def fix_params(self, method, params):
        params["client_id"] = self.key
        request_type = self.url[0:self.url.index(":")].lower()
        if request_type == "https":
            params["client_secret"] = self.secret
        elif request_type == "http":
            params["sign_time"] = int(time.time())
            params["sign_method"] = method
        self.params = params
        params["sign"] = self.gen_sign()
        return params

    def gen_sign(self):
        md5 = hashlib.md5()
        for i in self.params:
            md5.update(i)
        md5.digest()
        return md5.hexdigest()


if __name__ == '__main__':
    url = "Http://dilbmtcv.apihub.cn/api";
    key = "buwb2lii"
    secret = "ucr72ygfutspqeuu6s36"
    params = {"id": 1, "name": "allen"}
    prismClient = PrismClient(url, key, secret)
    print prismClient.doPost(params)
    print prismClient.doGet(params)
