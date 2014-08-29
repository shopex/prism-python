# __author__ = 'daixinyu'
# coding=utf8
import hashlib
import time
import urllib2
import urllib
from com.shopex.python.utils.UrlParser import UrlParser
from com.shopex.python.prism.PrismNotify import PrismNotify
from com.shopex.python.handler.PrismMessageHandler import PrismMessageHandler


class PrismClient:
    def __init__(self, url, key, secret):
        self.url = url
        self.key = key
        self.secret = secret
        self.url_info = UrlParser(self.url)
        self.params = ""

    def do_post(self, action, params):
        return self.run("POST", action, params)

    def do_get(self, action, params):
        return self.run("GET", action, params)

    def notify(self, method):
        return PrismNotify(self.url_info, method, PrismMessageHandler())

    def run(self, method, action, params):
        request_params = self.fix_params(method, params)
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
        if self.url_info.protocol == "https":
            params["client_secret"] = self.secret
        elif self.url_info.protocol == "http":
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