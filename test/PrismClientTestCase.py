# __author__ = 'daixinyu'
# coding=utf8

import unittest

from com.shopex.prism.PrismClient import PrismClient


class PrismClientTestCase(unittest.TestCase):
    def setUp(self):
        # self.url = "Http://localhost:3398"
        # self.url = "http://192.168.51.103:8899/api"
        self.url = "HTTP://dilbmtcv.apihub.cn/api";
        # self.url = "http://echo.websocket.org/"
        self.key = "buwb2lii"
        self.secret = "ucr72ygfutspqeuu6s36"
        self.prismClient = PrismClient(self.url, self.key, self.secret)

    # def testDoGet(self):
    # params = {}
    # print self.prismClient.do_get("/platform/notify/status", params)
    #
    #     #
    # def testDoPost(self):
    #     params = {"data": "hello"}
    #     print self.prismClient.do_post("/platform/notify/write", params)

    def testWebSocketConnect(self):
        method = "/platform/notify"
        prism_notify = self.prismClient.notify(method)
        prism_notify.consume()
        prism_notify.publish("order.new", "mytest00001")
        #
        #     # def testWebSocketConnect_2(self):
        #     # method = "/platform/notify"
        #     # prism_notify = self.prismClient.execute_notify(method)
        #     #     # prism_notify.consume()
        #     #     # prism_notify.publish("order.new", "mytest00001")


if __name__ == '__main__':
    unittest.main()
