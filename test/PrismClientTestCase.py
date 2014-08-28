# __author__ = 'daixinyu'
# coding=utf8

import unittest

from com.shopex.python.prism import PrismClient


class PrismClientTestCase(unittest.TestCase):

    def setUp(self):
        self.url = "Http://dilbmtcv.apihub.cn/api"
        self.key = "buwb2lii"
        self.secret = "ucr72ygfutspqeuu6s36"
        self.prismClient = PrismClient(self.url, self.key, self.secret)

    def testDoGet(self):
        params = {"id": 1, "name": "allen"}
        print self.prismClient.doGet("/platform/notify", params)

    def testDoPost(self):
        params = {"id": 1, "name": "allen"}
        print self.prismClient.doPost("/platform/notify", params)

if __name__ == '__main__':
    unittest.main()
