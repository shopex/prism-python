# __author__ = 'daixinyu'
# coding=utf8

import unittest
import json
import struct

from com.shopex.prism.PrismClient import PrismClient


class PrismMessageHandler():
    def __init__(self):
        pass

    #接受到Websocket服务端信息时触发调用
    def on_message(self, socket, message):
        print "[PrismMessageHandler] socket on_message!message is %s \t \n" % (message)
        json_message = json.loads(message)
        print "[on_message] %s \t \n" % (json_message)
        if json_message["tag"] == 1:#这里只对第一条消息做ACK应答
            print ("[PrismMessageHandler] send ack:%s" % (json_message["tag"]))
            socket.send(self.assemble_ack_date(json_message["tag"]))

    def assemble_ack_date(self, tag):
        return struct.pack("BB", 0x03, tag + 48)

    #Websocket连接关闭时触发调用
    def on_close(self, socket):
        print ("[PrismMessageHandler] on_close")

    # Websocket发生异常时触发调用
    def on_error(self, socket):
        print ("[PrismMessageHandler] on_error")


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
    #     params = {}
    #     print self.prismClient.do_get("/platform/notify/status", params)
    #
    #
    # def testDoPost(self):
    #     params = {"data": "hello"}
    #     print self.prismClient.do_post("/platform/notify/write", params)

    def testWebSocketConnect(self):
        method = "/platform/notify"
        prism_notify = self.prismClient.notify(method, PrismMessageHandler())
        prism_notify.consume()
        # prism_notify.publish("order.new", "mytest00001")


if __name__ == '__main__':
    unittest.main()
